# Локаторы
from selenium.webdriver.common.by import By


class RegisterPageLocators:
    # переменные для теста test_registration_page.py
    REGISTRATION_FORM_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # поле формы "Имя"
    REGISTRATION_FORM_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # поле формы "Email"
    REGISTRATION_FORM_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # поле формы "пароль"
    REGISTRATION_FORM_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    BUTTON_ENTER = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти" в форме личного кабинета
    TEXT_INVALID_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")  # Текст "Некорректный пароль"
    BUTTON_ENTER_REGISTRATION = (By.XPATH, ".//a[text()='Войти']") # Кнопка 'Войти'


class LoginPageLocators:
    # переменные для теста test_login_page.py
    LOGIN_FORM_EMAIL = (By.XPATH,
                        "//label[text()='Email']/following-sibling::input")  # поле формы "Email"
    LOGIN_FORM_PASSWORD = (By.XPATH,
                           "//label[text()='Пароль']/following-sibling::input")  # поле формы "Password"
    LOGIN_BUTTON_ENTER = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Вход" личного кабинета
    BUTTON_PERSONAL_CABINET = (
        By.XPATH, "//*[@id='root']/div/header/nav/a/p")  # Текст "Личный кабинет" на главной странице
    BUTTON_ENTER_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
    # странице
    BUTTON_ENTER_PASSWORD_RECOVERY = (By.XPATH, ".//a[text()='Войти']")  # Кнопка "Войти" в форме восстановления пароля


class MainPageLocators:
    TEXT_BUILD_A_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Кнопка "Войти" в форме восстановления парол


class PersonalCabPageLocators:
    # переменные для теста test_transition_to_personal_cabinet.py
    BUTTON_PERSONAL_CABINET = (
        By.XPATH, ".//a[contains(@href, '/account')]/p[text()='Личный Кабинет']")  # Текст "Личный кабинет" на главной
    # странице
    LOGIN_FORM_PASSWORD = (By.XPATH,
                           "//label[text()='Пароль']/following-sibling::input")  # поле формы "Пароль"
    LOGIN_FORM_EMAIL = (By.XPATH,
                        "//label[text()='Email']/following-sibling::input")  # поле формы "Email"
    LOGIN_BUTTON_EXIT = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Вход" личного кабинета


class PersonCabToLogoPageLocators:
    # переменные для теста test_from_personal_cabinet_to_constructor_and_to_logo.py
    BUTTON_PERSONAL_CABINET = (
        By.XPATH, "//*[@id='root']/div/header/nav/a/p")  # Текст "Личный кабинет" на главной странице
    BUTTON_CONSTRUCTOR = (
        By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p")  # Кнопка "Конструктор" на главной странице
    LOGO_STELLAR_BURGERS = (
        By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a")  # Лого "Stellar Burgers" на странице вход в
    # личный кабинет


class LogoutPageLocators:
    # переменные для теста test_logout_from_account.py
    BUTTON_PERSONAL_CABINET = (By.XPATH, "//body/div/div/header/nav/a")  # Текст "Личный кабинет" на главной странице

    LOGIN_FORM_EMAIL = (By.XPATH,
                        "//label[text()='Email']/following-sibling::input")  # поле формы "Email"
    LOGIN_FORM_PASSWORD = (By.XPATH,
                           "//label[text()='Пароль']/following-sibling::input")  # поле формы "Email"
    LOGIN_BUTTON_EXIT = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Вход" личного кабинета
    BUTTON_PERSONAL_CABINET_EXIT = (By.XPATH, ".//button[text()='Выход']")  # кнопка "Выход" личного кабинета
    TEXT_ENTER_PERSONAL_CABINET = (By.XPATH, ".//h2[text()='Вход']")  # Текст "Вход" страницы авторизации


class ConstructorPageLocators:
    # переменные для теста test_constructor_section.py
    TEXT_FILLINGS = (By.XPATH, ".//span[text()='Начинки']")  # Текст раздела "Начинки"
    PARENT_TEXT_FILLING = (By.XPATH, ".//span[text()='Начинки']/parent::div")  # Родитель текста раздела "Начинки"
    TEXT_SAUCES = (By.XPATH, ".//span[text()='Соусы']")  # Текст раздела "Соусы"
    PARENT_TEXT_SAUCES = (By.XPATH, ".//span[text()='Соусы']/parent::div")  # Родитель текста раздела "Соусы"
    TEXT_ROLLS = (By.XPATH, ".//span[text()='Булки']")  # Текст раздела "Булки"
    PARENT_TEXT_ROLLS = (By.XPATH, ".//span[text()='Булки']/parent::div")  # Родитель текста раздела "Булки"
