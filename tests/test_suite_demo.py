import unittest
from tests.login.login_tests import LoginPagePublishTests
from tests.landing.home_tests import HomePageTrivialTests
from tests.comment.comment_tests import CommentPageCommentTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginPagePublishTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(HomePageTrivialTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(CommentPageCommentTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)