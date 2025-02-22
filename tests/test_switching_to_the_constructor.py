#Переход из личного кабинета в конструктор
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from data import  Data
from locators import Locators


class TestSwitchingToConstructor:
    def test_switching_to_constructor_transition(self,driver, logined_driver):

        personal_account = driver.find_element(*Locators.STELLAR_BURGERS_PERSONAL_ACCOUNT)
        personal_account.click()  # нажать кнопку "Личный кабинет"

        WebDriverWait(driver, Data.WAIT_TIME).until (EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))

        constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
        constructor_button.click() # нажать кнопку "Конструктор"

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.text_to_be_present_in_element(Locators.BUILD_A_BURGER, Data.BUILD_A_BURGER_TEXT ))

        build_a_burger = driver.find_element(*Locators.BUILD_A_BURGER)

        assert build_a_burger.is_displayed() and build_a_burger.text == Data.BUILD_A_BURGER_TEXT

    def test_switching_to_constructor_via_logo(self, driver, logined_driver):

        personal_account = driver.find_element(*Locators.STELLAR_BURGERS_PERSONAL_ACCOUNT)
        personal_account.click()  # нажать кнопку "Личный кабинет"

        stellar_burgers_logo = driver.find_element(*Locators.STELLAR_BURGERS_LOGO)
        stellar_burgers_logo.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.text_to_be_present_in_element(Locators.BUILD_A_BURGER, Data.BUILD_A_BURGER_TEXT))

        build_a_burger = driver.find_element(*Locators.BUILD_A_BURGER)

        assert build_a_burger.is_displayed() and build_a_burger.text == Data.BUILD_A_BURGER_TEXT



