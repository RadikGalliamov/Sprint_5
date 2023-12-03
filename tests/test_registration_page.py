"""
Регистрация
Проверь:
Успешную регистрацию.
Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru.
Минимальный пароль — шесть символов.
Ошибку для некорректного пароля.
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .data import REGISTRATION_PAGE, name, email, password, random_email

REGISTRATION_FORM_NAME = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset/div/div/input")
REGISTRATION_FORM_EMAIL = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input")
REGISTRATION_FORM_PASSWORD = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[3]/div/div/input")
REGISTRATION_FORM_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
BUTTON_ENTER = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2[text()='Вход']")
TEXT_INVALID_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")

# Тесты на успешную регистрацию, с проверками на поля "Имя", "Email"
def test_successful_registration(browser):
    browser.get(REGISTRATION_PAGE)

    # Найди поле "Имя" и заполни его
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(REGISTRATION_FORM_NAME)).send_keys(name)

    # генерируем почту и сохраняем ее для проверки далее
    mail_generated = random_email

    # Найди поле "Email" и заполни его
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(REGISTRATION_FORM_EMAIL)).send_keys(mail_generated)

    # Найди поле "Пароль" и заполни его
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(REGISTRATION_FORM_PASSWORD)).send_keys(password)

    # Проверяем, что поле "Имя" не пустое
    assert browser.find_element(*REGISTRATION_FORM_NAME).get_attribute(
        "value") == name, "Ошибка в поле 'Имя'"

    # Проверяем, что email соответствует введенному
    assert browser.find_element(*REGISTRATION_FORM_EMAIL).get_attribute(
        "value") == mail_generated, "Ошибка в поле 'Email'"

    # Найди кнопку "Зарегистрироваться" и кликни по ней
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(REGISTRATION_FORM_BUTTON)).click()

    # Явное ожидание для загрузки страницы
    WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(BUTTON_ENTER))

    # Найди кнопку, получи её текст и проверь, что он равен 'Вход'
    assert browser.find_element(*BUTTON_ENTER).text == 'Вход', "Ошибка: не найдено значение кнопки 'Вход'"


# Тест на ошибку для некорректного пароля
@pytest.mark.parametrize("invalid_password", ['12345', 'abcde', '!@#$%', '12'], ids=["Negative test 12345",
                                                                                     "Negative test abcde",
                                                                                     "Negative test !@#$%",
                                                                                     "Negative test '12'"
                                                                                     ])
def test_invalid_password(browser, invalid_password):
    # Перейти на страницу регистрации
    browser.get(REGISTRATION_PAGE)

    # Заполнить поле "Имя"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(REGISTRATION_FORM_NAME)).send_keys(name)

    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(REGISTRATION_FORM_EMAIL)).send_keys(random_email)

    # Ввести пароль менее 6 символов
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(REGISTRATION_FORM_PASSWORD)).send_keys(invalid_password)

    # Нажать кнопку "Зарегистрироваться"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(REGISTRATION_FORM_BUTTON)).click()

    # Проверить, что появилась ошибка
    error_message = browser.find_element(*TEXT_INVALID_PASSWORD).text
    assert 'Некорректный пароль' in error_message, "Нет ошибки - 'Некорректный пароль'"
