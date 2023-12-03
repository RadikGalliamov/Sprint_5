"""
Переход по клику на «Конструктор» и на логотип Stellar Burgers.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .data import MAIN_PAGE

BUTTON_PERSONAL_CABINET = (By.XPATH, "//*[@id='root']/div/header/nav/a/p")
BUTTON_CONSTRUCTOR = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p")
LOGO_STELLAR_BURGERS = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a")


# Переход из личного кабинета в конструктор
def test_from_personal_cabinet_to_constructor(browser):
    # Переход на главную страницу
    browser.get(MAIN_PAGE)
    # Найти и нажать кнопку 'Личный кабинет'
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(BUTTON_PERSONAL_CABINET)).click()
    # Найти и нажать кнопку "Конструктор"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(BUTTON_CONSTRUCTOR)).click()
    assert MAIN_PAGE in browser.current_url, "MAIN_PAGE не найдена"


# Переход по клику на «Конструктор» и на логотип Stellar Burgers
def test_transition_to_constructor_via_constructor_button_and_logo(browser):
    # Переход на главную страницу
    browser.get(MAIN_PAGE)
    # Найти и нажать кнопку 'Личный кабинет'
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(BUTTON_PERSONAL_CABINET)).click()
    # Найти и нажать на лого "Stellar burgers"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(LOGO_STELLAR_BURGERS)).click()
    assert MAIN_PAGE in browser.current_url, "MAIN_PAGE не найдена"
