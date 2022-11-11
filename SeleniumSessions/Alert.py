import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
from webdrivermanager import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(
    executable_path="C:\\Users\\Arnab\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")

driver.implicitly_wait(5)
rediffurl = "https://mail.rediff.com/cgi-bin/login.cgi"
herokuapp = "https://the-internet.herokuapp.com/javascript_alerts"

"""
#REDIFFMAIL
driver.get(rediffurl)
driver.delete_all_cookies()
driver.maximize_window()

#Click on Sign in Button

SignIn = "//input[@value='Sign in']"
SignInButton = driver.find_element_by_xpath(SignIn)
SignInButton.click()

#Handling Alert
#driver.switch_to_alert()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.switch_to.default_content()
driver.quit()

"""

#HEROKUAPP

driver.get(herokuapp)
driver.delete_all_cookies()
driver.maximize_window()

PromptButton = driver.find_element_by_xpath("//button[text()='Click for JS Prompt']")
PromptButton.click()

alert = driver.switch_to.alert
print(alert.text)
time.sleep(5)
alert.send_keys('Hello')