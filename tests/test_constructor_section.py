"""
Проверь, что работают переходы к разделам:
«Булки»,
«Соусы»,
«Начинки».
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .data import MAIN_PAGE
from .locators import ConstructorPageLocators


# Переход к разделу "Начинки"
def test_navigation_to_buns_section_fillings(browser):
    # Переход на главную страницу
    browser.get(MAIN_PAGE)

    # Явное ожидание и клик по элементу
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(ConstructorPageLocators.TEXT_FILLINGS)
    ).click()

    # Явное ожидание и проверка появление элемента PARENT_TEXT_FILLING, при клике TEXT_FILLINGS меняется текст class
    # внутри PARENT_TEXT_FILLING
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(ConstructorPageLocators.PARENT_TEXT_FILLING)
    ), "элемент PARENT_TEXT_FILLING не найден"


# Переход к разделу "Соусы"
def test_navigation_to_buns_section_sauces(browser):
    # Переход на главную страницу
    browser.get(MAIN_PAGE)

    # Явное ожидание и клик по элементу
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(ConstructorPageLocators.TEXT_SAUCES)
    ).click()

    # Явное ожидание и проверка появление элемента PARENT_TEXT_SAUCES, при клике TEXT_SAUCES меняется текст class
    # внутри PARENT_TEXT_SAUCES
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(ConstructorPageLocators.PARENT_TEXT_SAUCES)
    ), "элемент PARENT_TEXT_SAUCES не найден"


# Переход к разделу "Булки"
def test_navigation_to_buns_section_rolls(browser):
    # Переход на главную страницу
    browser.get(MAIN_PAGE)

    # Явное ожидание и клик по элементу "Начинки"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(ConstructorPageLocators.TEXT_FILLINGS)
    ).click()

    # Явное ожидание и клик по элементу "Булки"
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(ConstructorPageLocators.TEXT_ROLLS)
    ).click()

    # Явное ожидание и проверка появление элемента PARENT_TEXT_ROLLS, при клике TEXT_ROLLS меняется текст class
    # внутри PARENT_TEXT_ROLLS
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(ConstructorPageLocators.PARENT_TEXT_ROLLS)
    ), "элемент PARENT_TEXT_ROLLS не найден"
