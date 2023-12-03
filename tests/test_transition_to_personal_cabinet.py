"""
Переход по клику на «Личный кабинет».
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .data import MAIN_PAGE, name, email

BUTTON_PERSONAL_CABINET = (By.XPATH, "//*[@id='root']/div/header/nav/a/p")
LOGIN_FORM_NAME = (By.XPATH,
                   "html/body/div/div/main/div/form/fieldset[@class='Auth_fieldset__1QzWN mb-6']/div/div/input[1]")
LOGIN_FORM_EMAIL = (By.XPATH,
                    "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
LOGIN_BUTTON_EXIT = (By.XPATH, ".//button[text()='Войти']")


# переход по клику на «Личный кабинет»
def test_logout_from_personal_cabinet_button(browser):
    # Перейти на главную страницу
    browser.get(MAIN_PAGE)

    # Нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(BUTTON_PERSONAL_CABINET)).click()

    # Заполнить поле "Имя"
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(LOGIN_FORM_NAME)).send_keys(name)

    # Заполнить поле "Email"
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(LOGIN_FORM_EMAIL)).send_keys(email)

    # Найти и нажать кнопку "Войти"
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(LOGIN_BUTTON_EXIT)).click()

    assert MAIN_PAGE in browser.current_url, "Ошибка: URL не совпадает с ожидаемым"
