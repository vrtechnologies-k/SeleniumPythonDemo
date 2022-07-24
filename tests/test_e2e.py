import time
from logging import getLogger

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.CheckoutPage import Checkoutpage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import Homepage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        homePage = Homepage(self.driver)
        log = self.getLogger()
        checkoutPage = homePage.shopItem()
        log.info("click on shop item")
        cards = checkoutPage.getCardTitles()

        count = len(cards)

        i = -1

        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            print(cardText)
            if cardText == "Nokia Edge":
                checkoutPage.getCardFooter()[i].click()
                log.info("Click on Nokia Edge Add footer")
                # self.driver.find_elements(By.CSS_SELECTOR, '.card-footer button')[i].click()

        checkoutPage.clickcheckout().click()
        # self.driver.find_element(By.XPATH, "//a[contains(@class,'btn-primary')]").click()

        confirmPage = checkoutPage.getbuttonsuccess()
        # self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()

        # time.sleep(10)

        confirmPage.getCountry().send_keys('Ind')
        # self.driver.find_element(By.ID, 'country').send_keys('Ind')

        self.verifyLinkTextPresent('India')

        log.info("Select the India from the Dropdown")

        #wait = WebDriverWait(self.driver, 10)

        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
        confirmPage.getCountryName().click()
        # self.driver.find_element(By.LINK_TEXT, 'India').click()

        time.sleep(5)
        confirmPage.selectchkbox().click()
        # self.driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox-primary']").click()

        time.sleep(5)
        confirmPage.getPurchase().click()
        # self.driver.find_element(By.CSS_SELECTOR, "input[class*='btn-success']").click()

        time.sleep(5)
        ordermsg = confirmPage.getSucmessage().text

        time.sleep(5)
        log.info(ordermsg)
        assert "Your order will be delivered in next few weeks" in ordermsg

    def test_two(self):
        print("Test two")
