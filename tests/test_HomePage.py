import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects import HomePage
from pageObjects.HomePage import Homepage
from utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homePage = Homepage(self.driver)
        homePage.getName().send_keys(getData["firstName"])
        log.info("enter firstName")
        homePage.getEmail().send_keys(getData["Email"])
        log.info("enter Email")
        homePage.getPassword().send_keys(getData["Password"])
        log.info("enter Password")
        homePage.getCheckBox().click()
        log.info("click on CheckBox")
        self.selectOptionByText(homePage.getGender(),getData["Gender"])
        log.info(getData["Gender"])
        homePage.getRadioButton().click()
        log.info("click on Radio Button")
        homePage.getBirthday().send_keys(getData["DOB"])
        log.info("Enter DOB")
        time.sleep(3)
        homePage.getSubmitButton().click()
        log.info("click on Purchase Button")
        sucMessage = homePage.getSuccessMessage().text

        log.info(sucMessage)
        assert "Success!" in sucMessage

        self.driver.refresh()
        time.sleep(5)

    #@pytest.fixture(params=[("venkat","venkat@gmail.com","venkat@123","Male","01-08-1988"),("Imam","Imam@gmail.com","Imam@123","Male","01-06-1991")])
    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self,request):
        return request.param
