from dotenv import load_dotenv
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import clean_user

# Setup environment
load_dotenv()
USERNAME = os.getenv('INSTA_USERNAME')
PASSWORD = os.getenv('INSTA_PASSWORD')
TARGET_USER = os.getenv('TARGET_USER')
ITERATION = int(os.getenv('ITERATION'))
CHECKPOINT = int(os.getenv('CHECKPOINT'))

# Setup selenium driver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Access instagram
url='https://www.instagram.com/'
driver.get(url)

# Login
time.sleep(5)
username=driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password=driver.find_element(By.CSS_SELECTOR, "input[name='password']")
username.clear()
password.clear()
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login.click()

# Go to profile
time.sleep(5)
post=TARGET_USER
driver.get(post)

# Go to Followers
time.sleep(5)
followers = driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
followers.click()

# Wait 10s for the dialog to load
time.sleep(10)

# Locate the dialog using a more specific XPath
dialog = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'xyi19xy')]")))

# Function to get usernames from the current view of the dialog
def get_usernames():
    usernames = set()
    span_elements = dialog.find_elements(By.CLASS_NAME, '_ap3a')
    for span in span_elements:
        usernames.add(span.text)
    return usernames

# Initial extraction of usernames
all_usernames = set()
new_usernames = get_usernames()
all_usernames.update(new_usernames)

checkpoint=0
scroll=0

def store_and_clear():
    # Store all collected usernames
    with open('users.txt', 'a') as file:
        # Write each user's name to the file followed by a newline
        for username in all_usernames:
            file.write(username + "\n")

    all_usernames.clear()

while True:

    # Scroll to the bottom of the container using JavaScript
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', dialog)
    time.sleep(5)

    # Extract new usernames and store in set
    new_usernames = get_usernames()
    all_usernames.update(new_usernames)

    scroll+=1
    checkpoint+=1
    print('step: '+str(scroll))

    # Checkpoint
    if checkpoint==CHECKPOINT:
        store_and_clear()
        checkpoint=0
        print('Stored!')

    # Check if new usernames are found
    if scroll==ITERATION:
        break

print("All usernames extracted:", all_usernames)

store_and_clear()
clean_user.remove_duplicates('users.txt', 'unique_users.txt')

# Close the driver
driver.quit()