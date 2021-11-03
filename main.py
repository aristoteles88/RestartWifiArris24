from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import os
import time
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('URL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

browser = webdriver.Safari()

browser.get(url=URL)

browser.implicitly_wait(10)

usernameField = browser.find_element(by=By.ID, value="UserName")
passwordField = browser.find_element(by=By.ID, value="Password")
applyButton = browser.find_element(by=By.CLASS_NAME, value="submitBtn")

usernameField.send_keys(USERNAME)
passwordField.send_keys(PASSWORD)
applyButton.click()

browser.implicitly_wait(15)
time.sleep(15)

# try:
#     enableWirelessPresent = presence_of_element_located((By.ID, "EnableWireless"))
#     WebDriverWait(browser, 20).until(enableWirelessPresent)
# except TimeoutError:
#     print("Não foi possível acessar a página")

enableWirelessCheckbox = browser.find_element(By.ID, "EnableWireless")
if enableWirelessCheckbox.is_enabled():
    enableWirelessCheckbox.click()

    browser.switch_to.alert.accept()

    applyButton = browser.find_element(by=By.CLASS_NAME, value="submitBtn")
    applyButton.click()

    browser.implicitly_wait(15)
    time.sleep(15)

    enableWirelessCheckbox = browser.find_element(By.ID, "EnableWireless")
enableWirelessCheckbox.click()

applyButton = browser.find_element(by=By.CLASS_NAME, value="submitBtn")
applyButton.click()

browser.close()
