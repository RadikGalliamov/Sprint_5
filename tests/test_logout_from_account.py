"""
Выход по кнопке «Выйти» в личном кабинете.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .data import MAIN_PAGE, email, password
from .locators import LogoutPageLocators


# Выход по кнопке «Выйти» в личном кабинете
def test_logout_from_personal_account(browser):
    # Переход на главную страницу
    browser.get(MAIN_PAGE)

    # Найти и нажать кнопку 'Личный кабинет'
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LogoutPageLocators.BUTTON_PERSONAL_CABINET)).click()

    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LogoutPageLocators.LOGIN_FORM_EMAIL)).send_keys(email)

    # Заполнить поле "password"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LogoutPageLocators.LOGIN_FORM_PASSWORD)).send_keys(password)

    # Найти и нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LogoutPageLocators.LOGIN_BUTTON_EXIT)
    ).click()

    # Найти и нажать кнопку 'Личный кабинет'
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LogoutPageLocators.BUTTON_PERSONAL_CABINET)
    ).click()

    # Найти и нажать текст 'Выйти'
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LogoutPageLocators.BUTTON_PERSONAL_CABINET_EXIT)
    ).click()

    # Проверка на отображение элемента текст 'Вход' страницы авторизации
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LogoutPageLocators.TEXT_ENTER_PERSONAL_CABINET)
    ).text == 'Вход', "Ошибка не получен текст 'Вход' страницы авторизации"

