import allure
import pytest
from data import AnswerBlock
from pages.main_page import MainPage


class TestQuestions:

    @allure.title('Проверка вопросов')
    @pytest.mark.parametrize(
        'num', [0, 1, 2, 3, 4, 5, 6, 7]
    )
    def test_click_question(self, driver, num):
        main_page = MainPage(driver)
        main_page.open_curl_samokat()
        main_page.click_to_question(num)
        assert main_page.get_answer(num) == AnswerBlock.type_of_answers[num]