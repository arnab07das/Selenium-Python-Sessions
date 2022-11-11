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
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.delete_all_cookies()
driver.maximize_window()

RightClick = "//span[text()='right click me']"
RightClickElement = driver.find_element_by_xpath(RightClick)

ac = ActionChains(driver)
ac.context_click(RightClickElement).perform()

RightClickOptions = "li.context-menu-icon"
RightClickOptionsElement = driver.find_elements_by_css_selector("li.context-menu-icon")
for element in RightClickOptionsElement:
    print(element.text)
    if element.text == "Copy":
        element.click()
        break





