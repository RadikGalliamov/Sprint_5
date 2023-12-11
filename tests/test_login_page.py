"""
вход по кнопке «Войти в аккаунт» на главной,
вход через кнопку «Личный кабинет»,
вход через кнопку в форме регистрации,
вход через кнопку в форме восстановления пароля.
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .data import MAIN_PAGE, LOGIN_PAGE, REGISTRATION_PAGE, name, email
from .locators import LoginPageLocators, RegisterPageLocators, MainPageLocators


# вход по кнопке «Войти в аккаунт» на главной странице
def test_login_from_main_page(browser):
    # Перейти на страницу логина
    browser.get(LOGIN_PAGE)
    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM_EMAIL)).send_keys(name)
    # Заполнить поле "Password"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM_PASSWORD)).send_keys(email)
    # Нажать кнопку "Войти"
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON_ENTER)).click()
    # Ждем появление элемента текст 'Собери бургер'
    assert WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            MainPageLocators.TEXT_BUILD_A_BURGER)), "Не найден элемент текст 'Соберите бургер' на главной странице"


# вход через кнопку Личный кабинет
def test_login_from_personal_cabinet_button(browser):
    # Перейти на главную страницу
    browser.get(MAIN_PAGE)
    # Найти и кликнуть кнопку «Личный кабинет»
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.BUTTON_PERSONAL_CABINET)).click()
    # Заполнить поле "Имя"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM_EMAIL)).send_keys(name)
    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM_PASSWORD)).send_keys(email)
    # Найти и нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON_ENTER)).click()
    # Ждем появление элемента текст 'Собери бургер'
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(
            MainPageLocators.TEXT_BUILD_A_BURGER)), "Не найден элемент текст 'Соберите бургер' на главной странице"


# вход через кнопку в форме регистрации
def test_login_from_registration_form_button(browser):
    # Перейти на страницу регистрации
    browser.get(REGISTRATION_PAGE)
    # Сделать прокрутку вниз
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(RegisterPageLocators.BUTTON_ENTER_REGISTRATION)).click()
    # Заполнить поле "Имя"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM_EMAIL)).send_keys(name)
    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM_PASSWORD)).send_keys(email)
    # Найти и нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON_ENTER)).click()
    # Ждем появление элемента текст 'Собери бургер'
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(
            MainPageLocators.TEXT_BUILD_A_BURGER)), "Не найден элемент текст 'Соберите бургер' на главной странице"


# вход через кнопку в форме восстановления пароля
def test_login_from_password_recovery_form_button(browser):
    # Перейти на страницу восстановления пароля
    browser.get(REGISTRATION_PAGE)
    # Нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(LoginPageLocators.BUTTON_ENTER_PASSWORD_RECOVERY)).click()
    # Заполнить поле "Имя"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM_EMAIL)).send_keys(name)
    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM_PASSWORD)).send_keys(email)
    # Найти и нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON_ENTER)).click()
    # Ждем появление элемента текст 'Собери бургер'
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(
            MainPageLocators.TEXT_BUILD_A_BURGER)), "Не найден элемент текст 'Соберите бургер' на главной странице"
