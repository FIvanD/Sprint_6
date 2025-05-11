from selenium.webdriver.common.by import By


class MainPageLocators:

    TEXT_WITH_QUESTION = By.ID, 'accordion__heading-{}'  # Локатор для вопроса (в {} порядковый номер)
    TEXT_WITH_ANSWER = By.ID, 'accordion__panel-{}'  # Локатор для ответа (в {} порядковый номер)
    THE_END_OF_PAGE = By.ID, 'accordion__heading-7' # Локатор для скролла в конец страницы