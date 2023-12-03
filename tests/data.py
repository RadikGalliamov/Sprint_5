# переменные с url проекта и данные для заполнения форм
import random

MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"
LOGIN_PAGE = "https://stellarburgers.nomoreparties.site/login"
REGISTRATION_PAGE = "https://stellarburgers.nomoreparties.site/register"
PASSWORD_RECOVERY_PAGE = "https://stellarburgers.nomoreparties.site/forgot-password"

name = "ivan_ivanov"
email = "ivan_ivanov_3_555@yandex.ru"
password = "111111"

# Генерируем случайное 3-значное число
random_number = random.randint(100, 999)
random_email = f"ivan_ivanov_3_{random_number}@yandex.ru"