#Раздел «Конструктор»

from locators import Locators

class TestConstructor:
    def test_constructor_buns(self, driver, logined_driver):

        constructor_toppings = driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS)
        constructor_toppings.click() # кликаем по табу "Начинки"

        constructor_buns = driver.find_element(*Locators.CONSTRUCTOR_BUNS)
        constructor_buns.click() # кликаем по табу "Булки"

        assert driver.find_element(*Locators.ATIVE_CONSTRUCTOR).text == "Булки"

    def test_constructor_sauces (self, driver, logined_driver):

        constructor_toppings = driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS)
        constructor_toppings.click() # клик по конструктору начинок

        constructor_sauces = driver.find_element(*Locators.CONSTRUCTOR_SAUCES)
        constructor_sauces.click() # клик по конструктору с соусами

        assert driver.find_element(*Locators.ATIVE_CONSTRUCTOR).text == "Соусы"

    def test_constructor_toppings (self, driver, logined_driver):

        constructor_toppings = driver.find_element(*Locators.CONSTRUCTOR_TOPPINGS)
        constructor_toppings.click()

        assert driver.find_element(*Locators.ATIVE_CONSTRUCTOR).text == "Начинки"

