import allure

from locators.drop_down_list_on_main_with_questions import MainPageLocators
from locators.navigate_for_order import ButtonLocators
from pages.base_page import BasePage
from data import ServiceUrl



class MainPage(BasePage):

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

    @allure.step('Клик на логотип Яндекс')
    def click_on_logo_yandex(self):
        self.click_on_element(ButtonLocators.BUTTON_YANDEX)


    @allure.step('Клик на логотип Самокат')
    def click_on_logo_samokat(self):
        self.click_on_element(ButtonLocators.BUTTON_SAMOKAT)

    @allure.step('Ожидание кнопки поиск')
    def wait_for_button_find(self):
        self.wait_for_element(ButtonLocators.BUTTON_FIND)
