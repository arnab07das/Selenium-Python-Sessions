import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium.webdriver import ActionChains
from webdrivermanager import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(
    executable_path="C:\\Users\\Arnab\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")

driver.implicitly_wait(5)
driver.get("https://www.flipkart.com/")
driver.delete_all_cookies()
driver.maximize_window()

#LOGIN TO FLIPKART

username = "//input[@class='_2IX_2- VJZDxU']"
password = "//input[@class='_2IX_2- _3mctLh VJZDxU']"
loginbutton = "//button[@type='submit'][@class='_2KpZ6l _2HKlqd _3AWRsL']"
driver.refresh()
driver.implicitly_wait(5)
driver.find_element_by_xpath(username).send_keys("8981569354")
driver.implicitly_wait(5)
driver.find_element_by_xpath(password).send_keys("Flipkart@2017")
driver.implicitly_wait(5)
driver.find_element_by_xpath(loginbutton).click()
time.sleep(5)

#MOUSE OVER TO FASHION >> WOMEN ETHNIC >> WOMEN SAREES

FashionDropDown = "//div[text()='Fashion']/*"
WomenEthnic = "//a[text()='Women Ethnic']"
WomenGowns = "//a[text()='Women Gowns']"
#WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[text()='Fashion']")))
FashionDropDownElement = driver.find_element_by_xpath(FashionDropDown)


ac = ActionChains(driver)
ac.move_to_element(FashionDropDownElement).perform()

WomenEthnicElement = driver.find_element_by_xpath(WomenEthnic)
driver.implicitly_wait(5)
ac.move_to_element(WomenEthnicElement).perform()

WomenGownsElement = driver.find_element_by_xpath(WomenGowns)
WomenGownsElement.click()
#ac = ActionChains(driver)
#ac.move_to_element(WomenGownsElement).perform().build().click()