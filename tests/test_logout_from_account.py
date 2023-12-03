"""
Выход по кнопке «Выйти» в личном кабинете.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .data import MAIN_PAGE, LOGIN_PAGE, email, password

BUTTON_PERSONAL_CABINET = (By.XPATH, "//body/div/div/header/nav/a")
LOGIN_FORM_NAME = (By.XPATH,
                   "html/body/div/div/main/div/form/fieldset[@class='Auth_fieldset__1QzWN mb-6']/div/div/input[1]")
LOGIN_FORM_EMAIL = (By.XPATH,
                    "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
LOGIN_BUTTON_EXIT = (By.XPATH, ".//button[text()='Войти']")
BUTTON_PERSONAL_CABINET_EXIT = (By.XPATH, ".//button[text()='Выход']")


# Выход по кнопке «Выйти» в личном кабинете
def test_logout_from_personal_account(browser):
    # Переход на главную страницу
    browser.get(MAIN_PAGE)

    # Найти и нажать кнопку 'Личный кабинет'
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(BUTTON_PERSONAL_CABINET)).click()

    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_FORM_NAME)).send_keys(email)

    # Заполнить поле "password"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_FORM_EMAIL)).send_keys(password)

    # Найти и нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_BUTTON_EXIT)
    ).click()

    # Найти и нажать кнопку 'Личный кабинет'
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(BUTTON_PERSONAL_CABINET)
    ).click()

    # Найти и нажать текст 'Выйти'
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(BUTTON_PERSONAL_CABINET_EXIT)
    ).click()

    # Явное ожидание url страницы логина
    WebDriverWait(browser, 10).until(
        EC.url_contains(LOGIN_PAGE)
    )
    assert LOGIN_PAGE in browser.current_url, "Ошибка: URL не совпадает с ожидаемым"
