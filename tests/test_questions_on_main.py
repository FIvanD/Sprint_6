import allure
import pytest
from data import AnswerBlock
from pages.main_page import MainPage
from data import ServiceUrl

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

    @allure.title('Проверка перехода по клику на лого Яндекса')
    def test_click_to_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.open_curl_samokat()
        main_page.click_on_logo_yandex()
        main_page.switch_to_new_window()
        main_page.wait_for_button_find()
        current_url = main_page.get_current_url()
        assert current_url == ServiceUrl.dzen_url


    @allure.title('Проверка перехода по клику на лого Самоката')
    def test_click_to_logo_samokat(self, driver):
        main_page = MainPage(driver)
        main_page.open_curl_samokat()
        main_page.click_on_logo_samokat()
        current_url = main_page.get_current_url()
        assert current_url == ServiceUrl.service_url