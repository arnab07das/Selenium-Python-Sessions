import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import exceptions
from selenium.webdriver.support.expected_conditions import staleness_of

driver = webdriver.Chrome(
    executable_path="C:\\Users\\Arnab\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://classic.freecrm.com/")
driver.delete_all_cookies()
driver.maximize_window()

username = "//input[@placeholder='Username']"
password = "//input[@placeholder='Password']"
loginbutton = "//input[@value='Login']"
driver.refresh()
driver.implicitly_wait(5)
driver.find_element_by_xpath(username).send_keys("arnab07das")
driver.implicitly_wait(5)
driver.find_element_by_xpath(password).send_keys("LEADAmuzic@07")
driver.implicitly_wait(5)
driver.find_element_by_xpath(loginbutton).click()

