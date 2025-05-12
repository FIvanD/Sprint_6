import allure
import pytest


from data import OrderData, ServiceUrl
from pages.main_page import MainPage
from pages.orders_page import OrderPage
from locators.navigate_for_order import OrderLocators
from locators.navigate_for_order import ButtonLocators


class TestOrders:

    @allure.title('Проверка оформления заказа')
    @pytest.mark.parametrize(
        "locator, order_data, button", [
            (OrderLocators.BUTTON_ORDER_MAIN, OrderData.DataForOrder1, ButtonLocators.BUTTON_COOKIE),
            (OrderLocators.BUTTON_ORDER_MIDDLE, OrderData.DataForOrder2, ButtonLocators.BUTTON_COOKIE)
        ]
    )
    def test_making_order_button(self, driver, locator, order_data, button):
        main_page = MainPage(driver)
        main_page.open_curl_samokat()
        main_page.click_on_element()
        main_page.click_button_order()
        order_page = OrderPage(driver)
        order_page.completion_fields(order_data)
        modal_complete = order_page.find_modal_window()
        assert modal_complete.is_displayed()

    @allure.title('Проверка перехода по клику на лого Яндекса')
    def test_click_to_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.open_curl_samokat()
        main_page.click_on_logo_yandex()
        main_page.wait_for_new_window_and_switch()
        assert "dzen.ru" in ServiceUrl.dzen_url


    @allure.title('Проверка перехода по клику на лого Самоката')
    def test_click_to_logo_samokat(self, driver):
        main_page = MainPage(driver)
        main_page.open_curl_samokat()
        main_page.click_on_logo_samokat()
        current_url = main_page.get_current_url()
        assert current_url == ServiceUrl.service_url