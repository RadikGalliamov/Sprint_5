"""
Переход по клику на «Конструктор» и на логотип Stellar Burgers.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import PersonCabToLogoPageLocators, MainPageLocators
from .data import MAIN_PAGE


# Переход из личного кабинета в конструктор
def test_from_personal_cabinet_to_constructor(browser):
    # Переход на главную страницу
    browser.get(MAIN_PAGE)
    # Найти и нажать кнопку 'Личный кабинет'
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(PersonCabToLogoPageLocators.BUTTON_PERSONAL_CABINET)).click()
    # Найти и нажать кнопку "Конструктор"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(PersonCabToLogoPageLocators.BUTTON_CONSTRUCTOR)).click()
    # Ждем появление элемента текст 'Собери бургер'
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(
            MainPageLocators.TEXT_BUILD_A_BURGER)), "Не найден элемент текст 'Соберите бургер' на главной странице"


# Переход из личного кабинета» на логотип Stellar Burgers
def test_transition_to_constructor_via_constructor_button_and_logo(browser):
    # Переход на главную страницу
    browser.get(MAIN_PAGE)
    # Найти и нажать кнопку 'Личный кабинет'
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(PersonCabToLogoPageLocators.BUTTON_PERSONAL_CABINET)).click()
    # Найти и нажать на лого "Stellar burgers"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(PersonCabToLogoPageLocators.LOGO_STELLAR_BURGERS)).click()
    # Ждем появление элемента текст 'Собери бургер'
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(
            MainPageLocators.TEXT_BUILD_A_BURGER)), "Не найден элемент текст 'Соберите бургер' на главной странице"
