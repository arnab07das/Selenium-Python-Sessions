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

#MOUSE OVER TO FASHION >> WOMEN ETHNIC >> WOMEN GOWNS

FashionDropDown = "//div[text()='Fashion']/*"
WomenEthnic = "//a[text()='Women Ethnic']"
WomenGowns = "//a[text()='Women Gowns']"

FashionDropDownElement = driver.find_element_by_xpath(FashionDropDown)
ac = ActionChains(driver)
ac.move_to_element(FashionDropDownElement).perform()

WomenEthnicElement = driver.find_element_by_xpath(WomenEthnic)
driver.implicitly_wait(5)
ac.move_to_element(WomenEthnicElement).perform()

WomenGownsElement = driver.find_element_by_xpath(WomenGowns)
WomenGownsElement.click()

#SELECT CHECKBOX FLIPKART ASSURED & 4* ABOVE

FAssured = "//img[@class='_3U-Vxu']//parent::div//parent::div//preceding-sibling::div[@class='_24_Dny _3tCU7L']"
driver.implicitly_wait(5)
driver.find_element_by_xpath(FAssured).click()

Fourstar = "//div[text()='4★ & above']//preceding-sibling::div[@class='_24_Dny']"
time.sleep(10)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='4★ & above']//preceding-sibling::div[@class='_24_Dny']"))).click()

#HANDLE THE RANGE SLIDER:


LeftHandle = "//div[@class='_31Kbhn _28DFQy']/div[@class='_3FdLqY']"
RightHandle = "//div[@class='_31Kbhn WC_zGJ']/div[@class='_3FdLqY']"

LeftHandleElement = driver.find_element_by_xpath(LeftHandle)
RightHandleElement = driver.find_element_by_xpath(RightHandle)

ac = ActionChains(driver)
time.sleep(10)
ac.drag_and_drop_by_offset(LeftHandleElement, 100, 0).perform()
ac.click_and_hold(LeftHandleElement).pause(1).move_by_offset(50, 0).release().perform()
ac.move_to_element(LeftHandleElement).pause(1).click_and_hold(LeftHandleElement).pause(1).move_by_offset(50, 0).release().perform()
