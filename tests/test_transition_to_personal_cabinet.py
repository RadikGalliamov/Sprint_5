"""
Переход по клику на «Личный кабинет».
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .data import MAIN_PAGE, email, password
from .locators import LoginPageLocators, PersonalCabPageLocators, MainPageLocators


# переход по клику на «Личный кабинет»
def test_logout_from_personal_cabinet_button(browser):
    # Перейти на главную страницу
    browser.get(MAIN_PAGE)

    # Нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.BUTTON_PERSONAL_CABINET)).click()

    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(PersonalCabPageLocators.LOGIN_FORM_EMAIL)).send_keys(email)

    # Заполнить поле "Пароль"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(PersonalCabPageLocators.LOGIN_FORM_PASSWORD)).send_keys(password)

    # Найти и нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(PersonalCabPageLocators.LOGIN_BUTTON_EXIT)).click()

    # Ждем появление элемента текст 'Собери бургер'
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(
            MainPageLocators.TEXT_BUILD_A_BURGER)), "Не найден элемент текст 'Соберите бургер' на главной странице"
