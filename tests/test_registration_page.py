"""
Регистрация
Проверь:
Успешную регистрацию.
Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru.
Минимальный пароль — шесть символов.
Ошибку для некорректного пароля.
"""
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .data import REGISTRATION_PAGE, name, password, random_email
from .locators import RegisterPageLocators


# Тесты на успешную регистрацию, с проверками на поля "Имя", "Email"
def test_successful_registration(browser):
    browser.get(REGISTRATION_PAGE)

    # Найди поле "Имя" и заполни его
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(RegisterPageLocators.REGISTRATION_FORM_NAME)).send_keys(name)

    # генерируем почту и сохраняем ее для проверки далее
    mail_generated = random_email

    # Найди поле "Email" и заполни его
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(RegisterPageLocators.REGISTRATION_FORM_EMAIL)).send_keys(mail_generated)

    # Найди поле "Пароль" и заполни его
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(RegisterPageLocators.REGISTRATION_FORM_PASSWORD)).send_keys(password)

    # Проверяем, что поле "Имя" не пустое
    assert browser.find_element(*RegisterPageLocators.REGISTRATION_FORM_NAME).get_attribute(
        "value") == name, "Ошибка в поле 'Имя'"

    # Проверяем, что email соответствует введенному
    assert browser.find_element(*RegisterPageLocators.REGISTRATION_FORM_EMAIL).get_attribute(
        "value") == mail_generated, "Ошибка в поле 'Email'"

    # Найди кнопку "Зарегистрироваться" и кликни по ней
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(RegisterPageLocators.REGISTRATION_FORM_BUTTON)).click()

    # Явное ожидание для загрузки страницы
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located(RegisterPageLocators.BUTTON_ENTER))

    # Найди кнопку, получи её текст и проверь, что он равен 'Вход'
    assert browser.find_element(
        *RegisterPageLocators.BUTTON_ENTER).text == 'Войти', "Ошибка: не найдено значение кнопки 'Войти'"


# Тест на ошибку для некорректного пароля
@pytest.mark.parametrize("invalid_password", ['12345'], ids=["Negative test 12345"])
def test_invalid_password(browser, invalid_password):
    # Перейти на страницу регистрации
    browser.get(REGISTRATION_PAGE)

    # Заполнить поле "Имя"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(RegisterPageLocators.REGISTRATION_FORM_NAME)).send_keys(name)

    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(RegisterPageLocators.REGISTRATION_FORM_EMAIL)).send_keys(random_email)

    # Ввести пароль менее 6 символов
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(RegisterPageLocators.REGISTRATION_FORM_PASSWORD)).send_keys(invalid_password)

    # Нажать кнопку "Зарегистрироваться"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(RegisterPageLocators.REGISTRATION_FORM_BUTTON)).click()

    # Проверить, что появилась ошибка
    error_message = browser.find_element(*RegisterPageLocators.TEXT_INVALID_PASSWORD).text
    assert 'Некорректный пароль' in error_message, "Нет ошибки - 'Некорректный пароль'"
