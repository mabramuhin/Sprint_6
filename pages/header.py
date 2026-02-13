import allure

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import DZEN_URL


class Header(BasePage, HeaderLocators):

    @allure.step("Нажать на логотип 'Самокат'")
    def click_scooter_logo(self):
        self.click_after_wait(self.scooter_logo)

    @allure.step("Нажать на логотип 'Яндекс'")
    def click_yandex_logo(self):
        self.click_after_wait(self.yandex_logo)

    @allure.step("Дождаться открытия главной страницы Дзена в новом окне")
    def switch_to_new_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(EC.url_to_be(DZEN_URL))
