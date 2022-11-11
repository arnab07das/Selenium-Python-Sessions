from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("--------------------------Setup------------------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")
    driver.maximize_window()
    yield
    print("--------------------------TearDown---------------------")
    driver.quit()


@pytest.mark.usefixtures("init_driver")
def test_validate_title():
    assert driver.title == "Google"


@pytest.mark.usefixtures("init_driver")
def test_validate_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"
