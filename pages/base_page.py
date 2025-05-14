import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Переход по ссылке')
    def go_to_curl(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента')
    def find_an_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Ввод текста в поле')
    def add_text_to_element(self, locator, text):
        self.find_an_element(locator).send_keys(text)

    @allure.step('Получение текста')
    def get_text_from_element(self, locator):
        return self.find_an_element(locator).text

    @allure.step('Изменение локатора')
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    @allure.step('Скролл страницы')
    def scroll_to_element(self, locator):
        element = self.find_an_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получение последней страницы в браузере')
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидание элемента')
    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Получение ссылки')
    def get_current_url(self):
        return self.driver.current_url
