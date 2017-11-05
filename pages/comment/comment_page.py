import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class CommentPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _blog = "//article[1]//h3"
    _comment= "//textarea[@id='comment']"               #textbox
    _comment_name= "//input[@id='author']"              #textbox
    _comment_email = "//input[@id='email']"             #textbox
    _post_comment = "//input[@id='submit']"             #button
    _add_reply_comment = "(//div[@class='reply'])[1]"
    usercomment= "(//footer//b)[1]"
    coo = "(//div[@id='comments']//div[1]/p)[1]"


    ### Element Interactions ###

    def clickBlog(self):
        self.elementClick(self._blog, locatorType="xpath")

    def enterComment(self, comment):
        self.sendKeys(comment, self._comment, locatorType="xpath")

    def enterCommentName(self, commentName):
        self.sendKeys(commentName, self._comment_name, locatorType="xpath")

    def enterCommentEmail(self, commentEmail):
        self.sendKeys(commentEmail,self._comment_email, locatorType="xpath")

    def clickPostComment(self):
        self.elementClick(self._post_comment, locatorType="xpath")

    def addReplyComment(self):
        self.elementClick(self._add_reply_comment, locatorType="xpath")



    def addComment(self, comment="", commentName="", commentEmail=""):
        self.clickBlog()
        self.enterComment(comment)
        self.enterCommentName(commentName)
        self.enterCommentEmail(commentEmail)
        self.clickPostComment()

    def addReplyComment(self, comment="", commentName="", commentEmail=""):
        self.addReplyComment()
        self.enterComment(comment)
        self.enterCommentName(commentName)
        self.enterCommentEmail(commentEmail)
        self.clickPostComment()


    def verifyNameForUser1(self):
         result1 = self.isElementPresent("//ol[@class='comment-list']//b[contains(text(), 'User 1')]",
                                        locatorType="xpath")
         return result1

    def verifyCommentForUser1(self):
         result2 = self.isElementPresent("//div[@class='comment-content']/p[contains(text(), 'Comment by user 1')]",
                                        locatorType="xpath")
         return result2


    def verifyNameForUser2(self):
         result1 = self.isElementPresent("//ol[@class='comment-list']//b[contains(text(), 'User 2')]",
                                        locatorType="xpath")
         return result1

    def verifyCommentForUser2(self):
         result2 = self.isElementPresent("//div[@class='comment-content']/p[contains(text(), 'Comment by user 2')]",
                                        locatorType="xpath")
         return result2



