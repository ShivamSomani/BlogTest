import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class HomePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    ### Element Interactions ###

    def verifyHtmlTag(self):
        result= self.isElementPresent("""//a[text()="user's Blog!"]""", locatorType="xpath")
        return result

    def verifyResponseCode(self):
        result = self.responseCode()
        return result
