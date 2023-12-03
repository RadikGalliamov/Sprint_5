"""
вход по кнопке «Войти в аккаунт» на главной,
вход через кнопку «Личный кабинет»,
вход через кнопку в форме регистрации,
вход через кнопку в форме восстановления пароля.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .data import MAIN_PAGE, LOGIN_PAGE, REGISTRATION_PAGE, name, email

LOGIN_FORM_NAME = (By.XPATH,
                   "html/body/div/div/main/div/form/fieldset[@class='Auth_fieldset__1QzWN mb-6']/div/div/input[1]")
LOGIN_FORM_EMAIL = (By.XPATH,
                    "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
LOGIN_BUTTON_EXIT = (By.XPATH, ".//button[text()='Войти']")
BUTTON_PERSONAL_CABINET = (By.XPATH, "//*[@id='root']/div/header/nav/a/p")
MAIN_PAGE_BUTTON_EXIT = (By.XPATH, "//*[@id='root']/div/main/div/div/p/a")


# вход по кнопке «Войти в аккаунт» на главной странице
def test_login_from_main_page(browser):
    # Перейти на страницу логина
    browser.get(LOGIN_PAGE)
    # Заполнить поле "Имя"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_FORM_NAME)).send_keys(name)
    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_FORM_EMAIL)).send_keys(email)
    # Нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_BUTTON_EXIT)).click()
    assert MAIN_PAGE in browser.current_url, "Ошибка: URL не совпадает с ожидаемым"


# вход через кнопку Личный кабинет
def test_login_from_personal_cabinet_button(browser):
    # Перейти на главную страницу
    browser.get(MAIN_PAGE)
    # Найти и кликнуть кнопку «Личный кабинет»
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(BUTTON_PERSONAL_CABINET)).click()
    # Заполнить поле "Имя"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_FORM_NAME)).send_keys(name)
    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_FORM_EMAIL)).send_keys(email)
    # Найти и нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_BUTTON_EXIT)).click()
    assert MAIN_PAGE in browser.current_url, "Ошибка: URL не совпадает с ожидаемым"


# вход через кнопку в форме регистрации
def test_login_from_registration_form_button(browser):
    # Перейти на главную страницу
    browser.get(REGISTRATION_PAGE)
    # Нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(MAIN_PAGE_BUTTON_EXIT)).click()
    # Заполнить поле "Имя"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_FORM_NAME)).send_keys(name)
    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_FORM_EMAIL)).send_keys(email)
    # Найти и нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_BUTTON_EXIT)).click()
    assert MAIN_PAGE in browser.current_url, "Ошибка: URL не совпадает с ожидаемым"


# вход через кнопку в форме восстановления пароля
def test_login_from_password_recovery_form_button(browser):
    # Перейти на страницу восстановления пароля
    browser.get(REGISTRATION_PAGE)
    # Нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(MAIN_PAGE_BUTTON_EXIT)).click()
    # Заполнить поле "Имя"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_FORM_NAME)).send_keys(name)
    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_FORM_EMAIL)).send_keys(email)
    # Найти и нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGIN_BUTTON_EXIT)).click()
    assert MAIN_PAGE in browser.current_url, "Ошибка: URL не совпадает с ожидаемым"
