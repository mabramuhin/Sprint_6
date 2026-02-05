import allure
import pytest

from pages.main_page import MainPage
from utils.constants import FAQ_ANSWERS


class TestMainPage:

    @allure.title("Проверка ответа на вопрос {question_index}")
    @pytest.mark.parametrize("question_index, expected_answer", FAQ_ANSWERS)
    def test_faq_answer_is_correct(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.open_question_accordion(question_index)
        actual_answer = main_page.get_answer_text(question_index)
        assert expected_answer == actual_answer
