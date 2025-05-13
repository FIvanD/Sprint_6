import allure

from locators.navigate_for_order import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):


    @allure.step('Оформление заказа')
    def completion_fields(self, data):

        self.add_text_to_element(OrderLocators.NAME_FIELD, data["name"])
        self.add_text_to_element(OrderLocators.FIRST_NAME_FIELD, data["first_name"])
        self.add_text_to_element(OrderLocators.ADDRESS_FIELD, data["address"])
        self.click_on_element(OrderLocators.METRO_STATION)
        self.add_text_to_element(OrderLocators.METRO_STATION, data["station"])
        self.click_on_element(OrderLocators.NAME_STATION)
        self.add_text_to_element(OrderLocators.PHONE_FIELD, data["phone"])
        self.click_on_element(OrderLocators.BUTTON_ORDER_NEXT)
        self.find_an_element(OrderLocators.DATA_FIELD)
        self.click_on_element(OrderLocators.DATA_FIELD)
        self.click_on_element(OrderLocators.CALENDAR)
        self.click_on_element(OrderLocators.TERM_FIELD)
        self.click_on_element(OrderLocators.DROPDOWN_DAYS)
        self.click_on_element(OrderLocators.GREY_CHECKBOX)
        self.add_text_to_element(OrderLocators.COMMENT_FIELD, data["comment"])
        self.click_on_element(OrderLocators.BUTTON_COMPLETE)
        self.click_on_element(OrderLocators.BUTTON_YES)

    @allure.step('Получение модального окна')
    def find_modal_window(self):
        return self.find_an_element(OrderLocators.MODAL_WINDOW)
