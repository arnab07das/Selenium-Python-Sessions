from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager

driver = None


def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")
    driver.maximize_window()


def teardown_module(module):
    driver.quit()


def test_validate_title():
    assert driver.title == "Google"


def test_validate_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"
