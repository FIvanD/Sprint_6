import allure
import pytest
import time

from data import OrderData, ServiceUrl
from pages.main_page import MainPage
from pages.orders_page import OrderPage
from locators.navigate_for_order import OrderLocators
from conftest import driver
from locators.navigate_for_order import ButtonLocators


class TestOrders:

    @allure.title('Проверка оформления заказа')
    @pytest.mark.parametrize(
        "locator, order_data", [
            (OrderLocators.BUTTON_ORDER_MAIN, OrderData.DataForOrder1),
            (OrderLocators.BUTTON_ORDER_MIDDLE, OrderData.DataForOrder2)
        ]
    )
    def test_making_order_button(self, driver, locator, order_data):
        button = ButtonLocators.BUTTON_COOKIE
        main_page = MainPage(driver)
        main_page.open_curl_samokat()
        try:
            main_page.click_on_element(button)
        except:
            pass
        main_page.click_button_order(locator)
        order_page = OrderPage(driver)
        order_page.completion_fields(order_data)
        modal_complete = order_page.find_modal_window()
        assert modal_complete.is_displayed()

    @allure.title('Проверка перехода по клику на лого Яндекса')
    def test_click_to_logo_yandex(self, driver):
        button = ButtonLocators.BUTTON_YANDEX
        main_page = MainPage(driver)
        main_page.open_curl_samokat()
        main_page.scroll_to_element(button)
        main_page.click_on_element(button)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        current_url = main_page.get_current_url()
        assert current_url == ServiceUrl.dzen_url


    @allure.title('Проверка перехода по клику на лого Самоката')
    def test_click_to_logo_samokat(self, driver):
        button = ButtonLocators.BUTTON_SAMOKAT
        main_page = MainPage(driver)
        main_page.open_curl_samokat()
        main_page.scroll_to_element(button)
        main_page.click_on_element(button)
        current_url = main_page.get_current_url()
        assert current_url == ServiceUrl.service_url