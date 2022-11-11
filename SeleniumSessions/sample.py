import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import exceptions
from selenium.webdriver.support.expected_conditions import staleness_of
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(
    executable_path="C:\\Users\\Arnab\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://www.google.com")
driver.delete_all_cookies()
driver.maximize_window()
driver.find_element_by_xpath("//input[@title='Search']").send_keys("Testing")
print(driver.title)
#webelements = driver.find_elements_by_xpath("//div[not(@id='shJ2Vb')]/ul[@class='G43f7e']/li/div/div/div[@class='wM6W7d']/span")
webelements = driver.find_elements_by_css_selector("div:not([id='shJ2Vb']) ul.G43f7e li div div div.wM6W7d span")
print("100")
for element in webelements:
    print(element.text)
    if element.text == 'testing tools':
        element.click()
        break

driver.quit()


