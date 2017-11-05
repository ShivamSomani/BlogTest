from pages.comment.comment_page import CommentPage
from utilities.teststatus import TestStatus
import unittest
import pytest, time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CommentPageCommentTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.cp = CommentPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=6)
    def test_addComment(self):
        self.cp.addComment("Comment by user 1", "User 1", "user1@typeset.io")
        result1 = self.cp.verifyNameForUser1()
        assert result1
        result2 = self.cp.verifyCommentForUser1()
        assert result2


    @pytest.mark.run(order=7)
    def test_addReplyComment(self):
        self.cp.addComment("Comment by user 2", "User 2", "user2@typeset.io")
        result1 = self.cp.verifyNameForUser2()
        assert result1
        result2 = self.cp.verifyCommentForUser2()
        assert result2


