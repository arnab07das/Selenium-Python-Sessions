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
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.delete_all_cookies()
driver.maximize_window()

Source = "//div[@id='draggable']"
Target = "//div[@id='droppable']"

SourceElement = driver.find_element_by_xpath("//div[@id='draggable']")
TargetElement = driver.find_element_by_xpath("//div[@id='droppable']")

ac = ActionChains(driver)
#ac.drag_and_drop(SourceElement, TargetElement).perform()
ac.click_and_hold(SourceElement).move_to_element(TargetElement).release().perform()
