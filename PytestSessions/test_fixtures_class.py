from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='class')
def init_chromedriver(request):
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = chrome_driver
    yield
    chrome_driver.quit()


@pytest.fixture(scope='class')
def init_geckodriver(request):
    gecko_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = gecko_driver
    yield
    gecko_driver.quit()


@pytest.fixture(scope='class')
def init_edgedriver(request):
    edge_driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    request.cls.driver = edge_driver
    yield
    edge_driver.quit()


@pytest.mark.usefixtures("init_geckodriver")
class Test_Parent:
    pass


class Test_Child(Test_Parent):

    def test_get_title(self):
        self.driver.get("http://www.google.com/")
        assert self.driver.title == "Google"

    def test_get_url(self):
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl"