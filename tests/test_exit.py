#Выход из аккаунта

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from data import  Data
from locators import Locators


class TestExit:
    def test_exit_in_personal_account(self, driver, logined_driver):

        personal_account = driver.find_element(*Locators.STELLAR_BURGERS_PERSONAL_ACCOUNT)
        personal_account.click()# нажать кнопку "Личный кабинет"

        WebDriverWait(driver,Data.WAIT_TIME).until(EC.url_to_be(Data.PROFILE_URL))

        exit_button = driver.find_element(*Locators.EXIT_BUTTON)
        exit_button.click() # нажать на кнопку "Выход"

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.STELLAR_BURGERS_LOGIN_BUTTON))

        assert driver.find_element (*Locators.STELLAR_BURGERS_LOGIN_BUTTON)


