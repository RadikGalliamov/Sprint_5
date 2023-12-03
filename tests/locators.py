# Локаторы

# переменные для теста test_registration_page.py
REGISTRATION_FORM_NAME = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset/div/div/input") # поле формы "Имя"
REGISTRATION_FORM_EMAIL = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input") # поле формы "Email"
REGISTRATION_FORM_PASSWORD = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[3]/div/div/input") # поле формы "пароль"
REGISTRATION_FORM_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
BUTTON_ENTER = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2[text()='Вход']") # Кнопка "Вход"
TEXT_INVALID_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']") # Текст "Некорректный пароль"

# переменные для теста test_login_page.py
LOGIN_FORM_NAME = (By.XPATH,
                   "html/body/div/div/main/div/form/fieldset[@class='Auth_fieldset__1QzWN mb-6']/div/div/input[1]") # поле формы "Имя"
LOGIN_FORM_EMAIL = (By.XPATH,
                    "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input") # поле формы "Email"
LOGIN_BUTTON_EXIT = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Вход" личного кабинета
BUTTON_PERSONAL_CABINET = (By.XPATH, "//*[@id='root']/div/header/nav/a/p") # Текст "Личный кабинет" на главной странице
MAIN_PAGE_BUTTON_EXIT = (By.XPATH, "//*[@id='root']/div/main/div/div/p/a") # Кнопка "Войти" на главной странице

# переменные для теста test_transition_to_personal_cabinet.py
BUTTON_PERSONAL_CABINET = (By.XPATH, "//*[@id='root']/div/header/nav/a/p") # Текст "Личный кабинет" на главной странице
LOGIN_FORM_NAME = (By.XPATH,
                   "html/body/div/div/main/div/form/fieldset[@class='Auth_fieldset__1QzWN mb-6']/div/div/input[1]") # поле формы "Имя"
LOGIN_FORM_EMAIL = (By.XPATH,
                    "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input") # поле формы "Email"
LOGIN_BUTTON_EXIT = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Вход" личного кабинета

# переменные для теста test_from_personal_cabinet_to_constructor_and_to_logo.py
BUTTON_PERSONAL_CABINET = (By.XPATH, "//*[@id='root']/div/header/nav/a/p") # Текст "Личный кабинет" на главной странице
BUTTON_CONSTRUCTOR = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p") # Кнопка "Конструктор" на главной странице
LOGO_STELLAR_BURGERS = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a") # Лого "Stellar Burgers" на главной странице

# переменные для теста test_logout_from_account.py
BUTTON_PERSONAL_CABINET = (By.XPATH, "//body/div/div/header/nav/a") # Текст "Личный кабинет" на главной странице
LOGIN_FORM_NAME = (By.XPATH,
                   "html/body/div/div/main/div/form/fieldset[@class='Auth_fieldset__1QzWN mb-6']/div/div/input[1]") # поле формы "Имя"
LOGIN_FORM_EMAIL = (By.XPATH,
                    "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input") # поле формы "Email"
LOGIN_BUTTON_EXIT = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Вход" личного кабинета
BUTTON_PERSONAL_CABINET_EXIT = (By.XPATH, ".//button[text()='Выход']") # кнопка "Выход" личного кабинета

# переменные для теста test_constructor_section.py
TEXT_FILLINGS = (By.XPATH, ".//span[text()='Начинки']") # Текст раздела "Начинки"
PARENT_TEXT_FILLING = (By.XPATH, ".//span[text()='Начинки']/parent::div") # Родитель текста раздела "Начинки"
TEXT_SAUCES = (By.XPATH, ".//span[text()='Соусы']") # Текст раздела "Соусы"
PARENT_TEXT_SAUCES = (By.XPATH, ".//span[text()='Соусы']/parent::div") # Родитель текста раздела "Соусы"
TEXT_ROLLS = (By.XPATH, ".//span[text()='Булки']") # Текст раздела "Булки"
PARENT_TEXT_ROLLS = (By.XPATH, ".//span[text()='Булки']/parent::div") # Родитель текста раздела "Булки"