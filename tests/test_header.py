import allure

from pages.header import Header
from utils.urls import MAIN_PAGE_URL, DZEN_URL


class TestHeader:

    @allure.title("Проверка перехода по клику на логотип 'Самокат'")
    def test_scooter_logo_redirect(self, driver):
        header = Header(driver)
        header.click_scooter_logo()
        assert header.get_current_url() == MAIN_PAGE_URL

    @allure.title("Проверка перехода по клику на логотип 'Яндекс'")
    def test_yandex_logo_redirect(self, driver):
        header = Header(driver)
        header.click_yandex_logo()
        header.switch_to_new_window()
        assert header.get_current_url() == DZEN_URL
