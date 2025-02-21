#Переход в личный кабинет

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from data import  Data
from locators import Locators

class TestTransferToAccount:
    def test_transfer_to_account_completed(self,driver,logined_driver):#Переход в личный кабинет

       personal_account = driver.find_element(*Locators.STELLAR_BURGERS_PERSONAL_ACCOUNT)
       personal_account.click()

       WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.CHANGE_PERSONAL_INFORMATION))

       assert driver.find_element(*Locators.CHANGE_PERSONAL_INFORMATION)

