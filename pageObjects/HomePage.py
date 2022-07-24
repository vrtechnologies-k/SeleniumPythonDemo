from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import Checkoutpage


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, 'Shop')
    name = (By.NAME,'name')
    email = (By.NAME, 'email')
    password = (By.ID,'exampleInputPassword1')
    checkbox = (By.ID,'exampleCheck1')
    gender = (By.ID,'exampleFormControlSelect1')
    radiobutton = (By.ID,'inlineRadio2')
    birthday = (By.NAME,'bday')
    submitButton = (By.CSS_SELECTOR,"[class*='btn-success']")
    successMessage = (By.CSS_SELECTOR,"[class*='alert-success']")

    def shopItem(self):
        self.driver.find_element(*Homepage.shop).click()
        checkoutPage = Checkoutpage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)

    def getPassword(self):
        return self.driver.find_element(*Homepage.password)

    def getCheckBox(self):
        return self.driver.find_element(*Homepage.checkbox)

    def getRadioButton(self):
        return self.driver.find_element(*Homepage.radiobutton)

    def getBirthday(self):
        return self.driver.find_element(*Homepage.birthday)

    def getSubmitButton(self):
        return self.driver.find_element(*Homepage.submitButton)

    def getSuccessMessage(self):
        return self.driver.find_element(*Homepage.successMessage)

    def getGender(self):
        return self.driver.find_element(*Homepage.gender)