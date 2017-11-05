import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//section[@id='meta-2']//a[text()='Log in']" #button
    _email_field = "//input[@id='user_login']"                  #textbox
    _password_field = "//input[@id='user_pass']"                #textbox
    _login_button = "//input[@id='wp-submit']"                  #button
    _add_new = "//li[@id='wp-admin-bar-new-content']/a/span[2]"
    _blog_title = "//label[@id='title-prompt-text']"            #textbox
    _blog_content = "//textarea[@id='content']"                 #textbox
    _publish_button = "//input[@id='publish']"                  #button
    _view_post = "//div[@id='message']/p/a"                     #button
    _view_blog_posted = "(//header[@class='entry-header']/h3[1]/a)[1]"
    _comment= "//textarea[@id='comment']"               #textbox
    _comment_name= "//input[@id='author']"              #textbox
    _comment_email = "//input[@id='email']"             #textbox
    _post_comment = "//input[@id='submit']"             #button
    usercomment= "(//footer//b)[1]"
    coo = "(//div[@id='comments']//div[1]/p)[1]"
    bold = "(//div[@class='entry-content']/p/b)[1]"

    ### Element Interactions ###

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def clickNew(self):
        self.elementClick(self._add_new, locatorType="xpath")

    def addBlogTitle(self, blogTitle):
        self.sendKeys(blogTitle, self._blog_title, locatorType= "xpath")

    def addBlogContent(self, blogContent):
        self.sendKeys(blogContent,self._blog_content, locatorType= "xpath" )

    def clickPublishButton(self):
        self.elementClick(self._publish_button, locatorType="xpath")

    def clickViewPost(self):
        self.elementClick(self._view_post, locatorType= "xpath")

    def clickViewBlogPosted(self):
        self.elementClick(self._view_blog_posted, locatorType="xpath")

    def enterComment(self, comment):
        self.sendKeys(comment, self._comment, locatorType="xpath")


    def enterNameInComment(self, name):
        self.sendKeys(name, self._comment_name, locatorType="xpath")


    def enterEmailInComment(self, email):
        self.sendKeys(email, self._comment_email, locatorType="xpath")

    def clickPostComment(self):
        self.elementClick(self._post_comment, locatorType= "xpath")




    #Publish1 Test
    def login(self, email="", password="", blogTitle="", blogContent=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        #self.clickCompose()
        self.clickNew()
        self.addBlogTitle(blogTitle)
        self.addBlogContent(blogContent)
        self.clickPublishButton()
        self.clickViewPost()

    #Publish Test (View Blog Posted by unauthenticated user)
    def verify(self):
        self.clickViewBlogPosted()

    #Comment1 Test
    def comment1(self, comment="", name="", email=""):
        self.clickViewBlogPosted()
        self.enterComment(comment)
        self.enterNameInComment(name)
        self.enterEmailInComment(email)
        self.clickPostComment()



    def verifyBlogTitle(self):
         result = self.isElementPresent("(//article[1]//h3/a[contains(text(), 'This is a blog by a test_user')])",
                                        locatorType="xpath")
         return result

    def verifyTextInBold(self):
         result = self.isElementPresent("//article[1]/div/p[contains(b/text(), 'anything')]",
                                        locatorType="xpath")
         return result



