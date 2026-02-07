import allure
from selenium.common import ElementClickInterceptedException
from locators.main_page_locators import MainPageLocators
from utils.enums import OrderEntryPoint
from pages.base_page import BasePage


class MainPage(BasePage, MainPageLocators):

    @allure.step("Открыть вопрос")
    def open_question_accordion(self, index):
        question_button = self.find_element_by_index(self.question_button, index)
        self.scroll_to_element(question_button)
        try:
            self.click_after_wait(question_button)
        except ElementClickInterceptedException:
            self.click_with_js(question_button)

    @allure.step("Получить текст ответа на вопрос")
    def get_answer_text(self, index):
        answer_panel = self.find_element_by_index(self.answer_panel, index)
        answer_text = self.wait_for_visibility_of(answer_panel).text
        return answer_text

    def click_order_button(self, entry_point: OrderEntryPoint):
        with allure.step(f"Нажать на кнопку 'Заказать' {entry_point.value}"):
            locator = getattr(self, entry_point.locator_name)
            self.click_after_wait(locator)
