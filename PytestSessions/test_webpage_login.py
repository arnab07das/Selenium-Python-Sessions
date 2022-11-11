from selenium import webdriver

def test_google_login():
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Arnab\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.get("http://www.google.com")
    assert driver.title == "Google"
    driver.quit()

def test_facebook_login():
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Arnab\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.get("http://www.facebook.com")
    assert driver.title == "Facebook"
    driver.quit()

def test_instagram_login():
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Arnab\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.get("http://www.instagram.com")
    assert driver.title == "Instagram"
    driver.quit()