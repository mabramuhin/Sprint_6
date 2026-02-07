import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import DZEN_URL


class BasePage:

    cookie_button = (By.CLASS_NAME, "App_CookieButton__3cvqF")
    scooter_logo = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    yandex_logo = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_for_visibility_of_element_located(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_presence_of_all_elements_located(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_visibility_of(self, element):
        return self.wait.until(EC.visibility_of(element))

    def wait_for_clickable(self, locator_or_element):
        return self.wait.until(EC.element_to_be_clickable(locator_or_element))

    def fill_input(self, locator, value):
        element = self.wait_for_visibility_of_element_located(locator)
        element.send_keys(value)

    def click_after_wait(self, locator_or_element):
        self.wait_for_clickable(locator_or_element).click()

    def click_with_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Подтвердить куки")
    def click_cookie_button(self):
        self.click_after_wait(self.cookie_button)

    def choose_from_dropdown(self, dropdown_locator, items_locator, index):
        self.click_after_wait(dropdown_locator)
        items = self.wait_for_presence_of_all_elements_located(items_locator)
        item = items[index]
        item.click()

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

    def find_element_by_index(self, locator, index):
        elements = self.driver.find_elements(*locator)
        return elements[index]

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
