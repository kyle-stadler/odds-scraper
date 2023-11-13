# Betting Picks with Text Notifications
## Overview

This Python application is designed to scrape sports betting picks from a specified website and send notifications via Twilio SMS when certain conditions are met. It is particularly useful for users who want to receive alerts about sports betting picks that meet specific rating criteria.

To date, this application has netted a 180% return on investment (bankroll) over a month of personal use.

## Prerequisites

Before using this application, you need to ensure that you have the following prerequisites in place:

  1. Python 3: Make sure you have Python 3 installed on your system.

  2. Selenium: Install the Selenium library, which is used for web scraping. You can install it using pip:

  ```
  pip install selenium
  ```

Chrome Web Browser: This application uses the Chrome web browser for scraping. Any browser can be used in it's place, selectors may need to be adjusted however. You'll need the ChromeDriver executable, which is included in the Selenium import.

Twilio Account: You must have a Twilio account to send SMS notifications. What's needed is a Twilio Account SID, Auth Token, and a Twilio phone number for sending messages.

Twilio Python Library: Install the Twilio Python library with the following command:

  ```
  pip install twilio
  ```
  personal_auth.py: Create a file named personal_auth.py and define the following constants within it:
  
    TWILIO_SID: # Your Twilio Account SID.
    
    TWILIO_AUTH: # Your Twilio Auth Token.
    
    SCRAPING_URL: # The URL of the website you want to scrape.
    
    SENDING_NUMBER: # Your Twilio phone number for sending SMS messages.
    
    RECEIVING_NUMBER: # The recipient's phone number for receiving SMS messages.

## Usage

  Run the application by executing the Python script.

    python app.py

  The application will open a headless Chrome browser and navigate to the specified SCRAPING_URL.

  It will locate the odds table on the webpage and extract the relevant data, including the sportsbook name.

  The application will then check the rating of the pick, and if it meets the defined criteria (e.g., a rating of 20 or higher), it will prepare a notification message.

  It checks if the pick is already logged in the picks.txt file. If the first 4 lines of the pick are not present in the file, it appends the pick to the file and sends an SMS notification if the rating is 50 or higher.

  The application will close the Chrome browser when it's finished.

## Configuration

You can adjust the behavior of the application by modifying the following constants within the script:

    TABLE_SELECTOR: The CSS selector for locating the odds table on the webpage.
    
    SPORTSBOOK_SELECTOR: The CSS selector for locating the sportsbook image metadata.
    
    rating #: The rating threshold for sending notifications.
    
    pick_lines: The number of lines to include in the notification message.
    
  You can customize the pick notification message format as needed.

## File Management

The application logs picks in a file named picks.txt. It checks if a pick with the same header (the first 4 lines) already exists in the file to prevent duplicates.
