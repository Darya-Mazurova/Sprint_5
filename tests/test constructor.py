#Раздел «Конструктор»
from copyreg import constructor

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from data import  Data
from locators import Locators

class TestConstructor:
    def test_constructor_buns(self, driver, logined_driver):

        constructor_toppings = driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS)
        constructor_toppings.click()

        constructor_buns = driver.find_element(*Locators.CONSTRUCTOR_BUNS)
        constructor_buns.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.BUNS))

        assert driver.find_element (*Locators.BUNS_CLASS)

    def test_constructor_sauces (self, driver, logined_driver):

        constructor_sauces = driver.find_element(*Locators.CONSTRUCTOR_SAUCES)
        constructor_sauces.click()
        assert driver.find_element (*Locators.SAUCES)


    def test_constructor_toppings (self, driver, logined_driver):

        constructor_toppings = driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS)
        constructor_toppings.click()
        assert driver.find_element (*Locators.TOPPINGS)

