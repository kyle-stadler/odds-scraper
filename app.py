from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twilio.rest import Client  # Import the Twilio client

# Initialize a headless browser (you can use a different browser if you prefer)
driver = webdriver.Chrome()

# Replace with the URL of the website you want to scrape
url = 'https://www.oddsshopper.com/odds/shop/?operatortype=sportsbook'
driver.get(url)

# Find the first dynamic <div> element with the specified class
div_element = driver.find_element(
    By.CSS_SELECTOR, 'div.os-table--col.line-col.MuiDataGrid-cell--withRenderer.MuiDataGrid-cell.MuiDataGrid-cell--textLeft.MuiDataGrid-withBorderColor')

# Find the first sportsbook image
sportsbook = driver.find_element(
    By.CSS_SELECTOR, 'img.MuiAvatar-img.css-1hy9t21')  # Fixed the CSS selector

# Your Twilio Account SID and Auth Token
account_sid = 'ACbe5f026453cd2028c877428417a3337e'
auth_token = 'c1bb955c7af60b5b837709897cd87811'

# Get the text of the first matching <div> element along with sportsbook info
parent_div = div_element.find_element(By.XPATH, './parent::div')
matching_text = parent_div.text
lines = matching_text.split('\n')

lines.pop(10)

rating = lines[6]
if int(rating) > 50:
    sportsbook_name = sportsbook.get_attribute("alt")
    # Construct the 'pick' variable with all lines except line 11
    pick_lines = lines[:10] + lines[11:]
    pick = "\n".join(pick_lines) + f"\nSportsbook: {sportsbook_name}"

    # Check if pick is already in the file
    with open('picks.txt', 'r') as file:
        existing_content = file.read()

        # Split pick and existing_content into lines
        pick_lines = pick.split('\n')[:3]  # Take the first 3 lines of pick
        existing_lines = existing_content.split(
            '\n')[:3]  # Take the first 3 lines

        first_three_lines = '\n'.join(existing_lines)

        if first_three_lines not in existing_content:
            # Append pick to the file
            with open('picks.txt', 'a') as file:
                file.write(pick)
                print("pick added to the file.")

            # Send a text using Twilio
            # message = client.messages.create(
            #     from_='+18339322565',
            #     body=pick,
            #     to='+14405032055'
            # )
            # print(f"Text message sent. SID: {message.sid}")

# Close the browser
driver.quit()
