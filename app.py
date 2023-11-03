from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize a headless browser (you can use a different browser if you prefer)
driver = webdriver.Chrome()

# Replace with the URL of the website you want to scrape
url = 'https://www.oddsshopper.com/odds/shop/?operatortype=sportsbook'
driver.get(url)

# Find all the dynamic <div> elements with the specified class
div_elements = driver.find_elements(
    By.CSS_SELECTOR, 'div.os-table--col.line-col.MuiDataGrid-cell--withRenderer.MuiDataGrid-cell.MuiDataGrid-cell--textLeft.MuiDataGrid-withBorderColor')

div_sportsbooks = driver.find_elements(
    By.CSS_SELECTOR, 'img.MuiAvatar-img.css-1hy9t21')  # Fixed the CSS selector

# Find and print the text of each matching <div> element along with sportsbook info
for div, sportsbook in zip(div_elements, div_sportsbooks):
    parent_div = div.find_element(By.XPATH, './parent::div')
    matching_text = parent_div.text
    sportsbook_name = sportsbook.get_attribute("alt")
    combined_text = f"\n{matching_text}\nSportsbook: {sportsbook_name}"
    print(combined_text)

# Close the browser
driver.quit()
