#Регистрация
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data

from locators import Locators

class TestRegistration:
    def test_registration_successful (self, driver): #Успешная регистрация

        login_to_account = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON)
        login_to_account.click() # нажать кнопку "Войти в аккаунт"

        registration_link = driver.find_element(*Locators.STELLAR_BURGERS_REGISTRATION_LINK)
        registration_link.click() # нажать на ссылку "Зарегистрироваться"

        registration_name = driver.find_element(*Locators.STELLAR_BURGERS_REGISTRATION_NAME)
        registration_name.send_keys(Data.STELLAR_BURGERS_NAME_USER) # вести  имя

        registration_email = driver.find_element(*Locators.STELLAR_BURGERS_REGISTRATION_EMAIL)
        registration_email.send_keys(Data.STELLAR_BURGERS_EMAIL_USER) # ввести email

        registration_password = driver.find_element(*Locators.STELLAR_BURGERS_REGISTRATION_PASSWORD)
        registration_password.send_keys(Data.STELLAR_BURGERS_PASSWORD)# ввести пароль

        registration_button = driver.find_element(*Locators.STELLAR_BURGERS_REGISTRATION_BUTTON)
        registration_button.click() # нажать кнопку "Зарегистрироваться"

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STELLAR_BURGERS_LOGIN_BUTTON))

        assert driver.find_element(*Locators. STELLAR_BURGERS_LOGIN_BUTTON) \

    def test_registration_incorrect_password (self, driver):#Ошибкa для некорректного пароля
        login_to_account = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON)
        login_to_account.click()  # нажать кнопку "Войти в аккаунт"

        registration_link = driver.find_element(*Locators.STELLAR_BURGERS_REGISTRATION_LINK)
        registration_link.click()  # нажать на ссылку "Зарегистрироваться"

        registration_name = driver.find_element(*Locators.STELLAR_BURGERS_REGISTRATION_NAME)
        registration_name.send_keys(Data.STELLAR_BURGERS_NAME_USER)  # вести  имя

        registration_email = driver.find_element(*Locators.STELLAR_BURGERS_REGISTRATION_EMAIL)
        registration_email.send_keys(Data.STELLAR_BURGERS_EMAIL_USER)  # ввести email

        registration_password = driver.find_element(*Locators.STELLAR_BURGERS_REGISTRATION_PASSWORD)
        registration_password.send_keys(Data.STELLAR_BURGERS_PASSWORD_FAILD)  # ввести пароль

        registration_button = driver.find_element(*Locators.STELLAR_BURGERS_REGISTRATION_BUTTON)
        registration_button.click()  # нажать кнопку "Зарегистрироваться"



        assert driver.find_element(*Locators. INCORRECT_PASSWORD_MASSAGE)