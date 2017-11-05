from pages.Login.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginPagePublishTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

#- Given-- Adding a new blog
    @pytest.mark.run(order=3)
    def test_addNewBlog(self):
        self.lp.login("test_user", "testuser@123", "This is a blog by a test_user", "Test user likes to blog. The content of the blog can be <b> anything </b>")

# @Test- unauthenticated users should be able to see the blog title on the blog index page.
    @pytest.mark.run(order=4)
    def test_verifyBlogTitle(self):
        result=self.lp.verifyBlogTitle()
        assert result == True



# @Test- viewing the blog should show the “anything” in bold
    @pytest.mark.run(order=5)
    def test_verifyTextInBold(self):
        result= self.lp.verifyTextInBold()
        assert result == True
