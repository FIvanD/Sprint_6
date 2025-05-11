import allure

from locators.drop_down_list_on_main_with_questions import MainPageLocators
from pages.foundation_page import FoundationPage
from data import ServiceUrl



class MainPage(FoundationPage):

    @allure.step('Переход по ссылке')
    def open_curl_samokat(self):
        self.go_to_curl(ServiceUrl.service_url)


    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_format = self.format_locators(MainPageLocators.TEXT_WITH_QUESTION, num)
        self.scroll_to_element(MainPageLocators.THE_END_OF_PAGE)
        self.click_on_element(locator_format)


    @allure.step('Получение ответа')
    def get_answer(self, num):
        locator_format = self.format_locators(MainPageLocators.TEXT_WITH_ANSWER, num)
        return self.get_text_from_element(locator_format)


    @allure.step('Клик по кнопке заказать на главной странице')
    def click_button_order(self, locator):
        self.find_an_element(locator)
        self.scroll_to_element(locator)
        self.click_on_element(locator)

