import pytest
from selenium import webdriver

from pages.main_page import MainPage
from utils.constants import MAIN_PAGE_URL


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(MAIN_PAGE_URL)
    main_page = MainPage(driver)
    main_page.click_cookie_button()

    yield driver
    driver.quit()
