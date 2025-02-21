import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators
@pytest.fixture(scope='function')
def driver ():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.STELLAR_BURGERS_URL)

    yield chrome_driver


    chrome_driver.quit()

@pytest.fixture(scope='function')
def logined_driver (driver):

    login_to_account = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON)
    login_to_account.click()  # нажать кнопку "Войти в аккаунт"

    email_input = driver.find_element(*Locators.STELLAR_BURGERS_EMAIL_INPUT)
    email_input.send_keys(Data.STELLAR_BURGERS_LOGIN)  # ввести логин

    password_input = driver.find_element(*Locators.STELLAR_BURGERS_PASSWORD_INPUT)
    password_input.send_keys(Data.STELLAR_BURGERS_PASSWORD)  # ввести пароль

    enter_button = driver.find_element(*Locators.STELLAR_BURGERS_LOGIN_BUTTON)
    enter_button.click()  # нажать кнопку "Войти"

    WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.THE_CHECKOUT_BUTTON))

    yield driver





