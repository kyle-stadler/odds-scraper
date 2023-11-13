from selenium import webdriver
from selenium.webdriver.common.by import By
from twilio.rest import Client

# Constants
SCRAPING_URL = 'https://www.oddsshopper.com/odds/shop/?operatortype=sportsbook'
TWILIO_SID = 'ACbe5f026453cd2028c877428417a3337e'
TWILIO_AUTH = 'c1bb955c7af60b5b837709897cd87811'

# Initialize a headless browser
driver = webdriver.Chrome()
driver.get(SCRAPING_URL)

# The div that I'm looking to scrape is the one that all the data within the odds table shares
div_element = driver.find_element(
    By.CSS_SELECTOR, 'div.os-table--col.line-col.MuiDataGrid-cell--withRenderer.MuiDataGrid-cell.MuiDataGrid-cell--textLeft.MuiDataGrid-withBorderColor')

# Finding sportsbook image metadata since it has a different selector than the others
sportsbook = driver.find_element(
    By.CSS_SELECTOR, 'img.MuiAvatar-img.css-1hy9t21')

# Extracting the text that is within the divs, the text is equal to each cell within the odds table
parent_div = div_element.find_element(By.XPATH, './parent::div')
matching_text = parent_div.text

# Splitting the total text into lines so I can adjust what data to include easier
lines = matching_text.split('\n')

rating = lines[6]
if int(rating) >= 20:
    sportsbook_name = sportsbook.get_attribute("alt")
    # Gets rid of the last two lines which is the sportsbook bonus and time it's been up
    pick_lines = lines[:11]
    pick = "\n".join(pick_lines) + f"\nSportsbook: {sportsbook_name}\n\n"

    # Create the Twilio client
    client = Client(TWILIO_SID, TWILIO_AUTH)

    # Check if pick is already in the file
    with open('picks.txt', 'r', encoding='utf-8') as file:
        logged_picks = file.read()

        # Here i'm only checking if the first 4 lines of each pick are already logged (League, Team/player, Time/date, Bet Type)
        pick_lines = pick.split('\n')[:4]  # Take the first 4 lines of pick

        pick_header = '\n'.join(pick_lines)

        if pick_header not in logged_picks:
            # Append pick to the file
            with open('picks.txt', 'a', encoding='utf-8') as file:
                file.write(pick)

            # Send a text using Twilio
            # if int(rating) >= 50:
            #     message = client.messages.create(
            #         from_='+18339322565',
            #         body=pick,
            #         to='+14405032055'
            #     )
            #     print(f"Text message sent. SID: {message.sid}")

# Close the browser
driver.quit()
