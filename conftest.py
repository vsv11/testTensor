import pytest
from selenium import webdriver

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://sbis.ru')
    yield driver
    driver.quit()

