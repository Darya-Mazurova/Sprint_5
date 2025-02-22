#Вход
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from data import  Data
from locators import Locators


class TestLogin:
    def test_login_in_via_the_personal_account_button(self, driver): #вход через кнопку «Личный кабинет»

        personal_account = driver.find_element(*Locators.STELLAR_BURGERS_PERSONAL_ACCOUNT)
        personal_account.click() # нажать кнопку "Личный кабинет"

        email_input = driver.find_element(*Locators.STELLAR_BURGERS_EMAIL_INPUT)
        email_input.send_keys(Data.STELLAR_BURGERS_LOGIN) # ввести логин

        password_input = driver.find_element(*Locators.STELLAR_BURGERS_PASSWORD_INPUT)
        password_input.send_keys(Data.STELLAR_BURGERS_PASSWORD) # ввести пароль


        enter_button = driver.find_element(*Locators.STELLAR_BURGERS_LOGIN_BUTTON)
        enter_button.click()# нажать кнопку "Войти"

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.THE_CHECKOUT_BUTTON))

        the_checkout_button = driver.find_element(*Locators.THE_CHECKOUT_BUTTON)

        assert the_checkout_button.is_displayed()

    def test_login_by_clicking_log_in_to_your_account(self, driver):#вход по кнопке «Войти в аккаунт» на главной
        login_to_account = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON)
        login_to_account.click()

        email_input = driver.find_element(*Locators.STELLAR_BURGERS_EMAIL_INPUT)
        email_input.send_keys(Data.STELLAR_BURGERS_LOGIN)  # ввести логин

        password_input = driver.find_element(*Locators.STELLAR_BURGERS_PASSWORD_INPUT)
        password_input.send_keys(Data.STELLAR_BURGERS_PASSWORD)

        enter_button = driver.find_element(*Locators.STELLAR_BURGERS_LOGIN_BUTTON)
        enter_button.click()  # нажать кнопку "Войти"

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.THE_CHECKOUT_BUTTON))

        the_checkout_button = driver.find_element(*Locators.THE_CHECKOUT_BUTTON)

        assert the_checkout_button.is_displayed()


        # ввести пароль
        #вход по кнопке «Войти в аккаунт» на главной

    def test_login_via_the_button_in_the_registration_form(self, driver):# вход по кнопке в форме регистрации

        login_to_account = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON)
        login_to_account.click()

        registration_link = driver.find_element(*Locators.STELLAR_BURGERS_REGISTRATION_LINK)
        registration_link.click()

        login_to_account_link = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_LINK)
        login_to_account_link.click()

        email_input = driver.find_element(*Locators.STELLAR_BURGERS_EMAIL_INPUT)
        email_input.send_keys(Data.STELLAR_BURGERS_LOGIN)  # ввести логин

        password_input = driver.find_element(*Locators.STELLAR_BURGERS_PASSWORD_INPUT)
        password_input.send_keys(Data.STELLAR_BURGERS_PASSWORD)

        enter_button = driver.find_element(*Locators.STELLAR_BURGERS_LOGIN_BUTTON)
        enter_button.click()  # нажать кнопку "Войти"

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.THE_CHECKOUT_BUTTON))

        the_checkout_button = driver.find_element(*Locators.THE_CHECKOUT_BUTTON)

        assert the_checkout_button.is_displayed()


        # вход по кнопке в форме регистрации

    def test_login_through_the_button_in_the_password_recovery_form(self, driver):#вход через кнопку в форме восстановления пароля
        login_to_account = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON)
        login_to_account.click()

        password_recovery = driver.find_element(*Locators.PASSWORD_RECOVERY_LINK)
        password_recovery.click()

        login_to_account_link = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_LINK)
        login_to_account_link.click()

        email_input = driver.find_element(*Locators.STELLAR_BURGERS_EMAIL_INPUT)
        email_input.send_keys(Data.STELLAR_BURGERS_LOGIN)  # ввести логин

        password_input = driver.find_element(*Locators.STELLAR_BURGERS_PASSWORD_INPUT)
        password_input.send_keys(Data.STELLAR_BURGERS_PASSWORD)

        enter_button = driver.find_element(*Locators.STELLAR_BURGERS_LOGIN_BUTTON)
        enter_button.click()  # нажать кнопку "Войти"

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.THE_CHECKOUT_BUTTON))

        the_checkout_button = driver.find_element(*Locators.THE_CHECKOUT_BUTTON)

        assert the_checkout_button.is_displayed()
        #вход через кнопку в форме восстановления пароля