from selenium.webdriver.common.by import By


class ButtonLocators:

    BUTTON_YANDEX = By.XPATH, '//a[@href = "//yandex.ru"]'
    BUTTON_SAMOKAT = By.XPATH, '//a[@href= "/"]'
    BUTTON_COOKIE = By.XPATH, '//button[text()= "да все привыкли"]'
    BUTTON_FIND = By.XPATH, '//button[text()="Найти"]'

class OrderLocators:

    BUTTON_ORDER_MAIN = By.CLASS_NAME, 'Button_Button__ra12g'
    BUTTON_ORDER_MIDDLE = By.CSS_SELECTOR, '.Button_Button__ra12g.Button_Middle__1CSJM'

    METRO_STATION = By.XPATH, '//input[@placeholder="* Станция метро"]'
    BUTTON_ORDER_NEXT = By.XPATH, '//button[text()= "Далее"]'
    NAME_FIELD = By.XPATH, '//input[@placeholder="* Имя"]'
    FIRST_NAME_FIELD = By.XPATH, '//input[@placeholder="* Фамилия"]'
    ADDRESS_FIELD = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    PHONE_FIELD = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    DATA_FIELD = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    CALENDAR = By.XPATH, '//*[text()="30"]'
    TERM_FIELD = By.CLASS_NAME, 'Dropdown-placeholder'
    DROPDOWN_DAYS = By.XPATH, '//*[text()="сутки"]'
    GREY_CHECKBOX = By.ID, 'grey'
    BLACK_CHECKBOX = By.ID, 'black'
    COMMENT_FIELD = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    BUTTON_COMPLETE = By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]'
    BUTTON_YES = By.XPATH, '//button[text()="Да"]'
    MODAL_WINDOW = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'

    NAME_STATION = By.XPATH, '//*[@class="select-search__select"]'
