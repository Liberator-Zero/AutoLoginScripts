import win32cred
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Retrieve credentials from Windows Credential Manager
creds = win32cred.CredRead("InsertWinCredNameHere", win32cred.CRED_TYPE_GENERIC)
username = creds['UserName']
password = creds['CredentialBlob'].decode()

# Set up the Firefox driver
driver = webdriver.Firefox()

# Open the portal login page
driver.get("InsertURLHere")

# Wait until the username and password fields are present, then enter credentials
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
username_field.send_keys(username)

password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_field.send_keys(password)

# Locate and click the login button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)
login_button.click()

# Optional: Wait to ensure login completes
time.sleep(5)

# No driver.quit() here so the browser remains open
