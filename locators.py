from selenium.webdriver.common.by import By


class Locators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH,"// button[text() = 'Войти в аккаунт']") #кнопка "Войти в аккаунт" на главной странице сервиса

    STELLAR_BURGERS_PERSONAL_ACCOUNT = (By.XPATH,"//a[@href='/account']") # кнопка "Личный кабинет"

    STELLAR_BURGERS_EMAIL_INPUT=(By.XPATH,"//input[@class='text input__textfield text_type_main-default']") # поле ввода логина (email)
    STELLAR_BURGERS_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']") # поле ввода пароля

    STELLAR_BURGERS_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # кнопка "Войти" на странице авторизации

    STELLAR_BURGERS_REGISTRATION_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Зарегистрироваться']") # ссылка на форму регистрации

    STELLAR_BURGERS_REGISTRATION_NAME = (By.XPATH, "//*[@id='root']//input") # поле ввода имени при регистрации
    STELLAR_BURGERS_REGISTRATION_EMAIL = (By.XPATH, "//form/fieldset[2]//input")# поле ввода email при регистрации
    STELLAR_BURGERS_REGISTRATION_PASSWORD = (By.XPATH, "//input[@name='Пароль']")# поле ввода пароля при регистрации

    STELLAR_BURGERS_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")# кнопка регистрации

    INCORRECT_PASSWORD_MASSAGE = (By.XPATH, "//p[text()='Некорректный пароль']") # ошибка при некорректном пароле

    THE_CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")# кнопка оформить заказ

    LOGIN_TO_ACCOUNT_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']")# ссылка на страницу авторизации

    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")#ссылка на страницу восстановления пароля

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")# кнопка "Конструктор"
    BUILD_A_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")# заголовок конструктора - Собери бургер

    CHANGE_PERSONAL_INFORMATION = (By.XPATH, "//p[text() = 'В этом разделе вы можете изменить свои персональные данные']") # "Личный кабинет"

    EXIT_BUTTON = (By.XPATH,"//button[text() = 'Выход']")  # кнопка выхода из аккаунта

    CONSTRUCTOR_BUNS = (By.XPATH,"//span[text()='Булки']") # конструктор с булками

    CONSTRUCTOR_TOPPINGS= (By.XPATH, "//span[text()='Начинки']") # конструктор с начинками

    CONSTRUCTOR_SAUCES = (By.XPATH,"//span[text()='Соусы']") #конструктор с соусами

    STELLAR_BURGERS_LOGO= (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2' ]") # главный логотип

    ATIVE_CONSTRUCTOR =  (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]') # класс активного конструктора