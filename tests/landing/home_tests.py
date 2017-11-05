from pages.landing.home_page import HomePage
from pages.Login.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class HomePageTrivialTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=1)
    def test_verifyResponseCode(self):
        result = self.hp.verifyResponseCode()
        assert result == 200
        print(result)


    @pytest.mark.run(order=2)
    def test_verifyHtmlTag(self):
        result = self.hp.verifyHtmlTag()
        print(result)
        assert result == True