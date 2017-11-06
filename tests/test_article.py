import unittest
from app.models import Article

class TestArticle(unittest.TestCase):

    def setUp(self):
        self.new_article = Article('python 101')


    def tearDown(self):
        Article.clear_articles()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_article.body,'python 101')


    def test_save_article(self):
        self.new_article.save_article()
        self.assertTrue(len(Article.all_articles)>0)


    def test_get_article_by_id(self):

        self.new_article.save_article()
        got_articles = Review.get_reviews(12345)
        self.assertTrue(len(got_articles) == 1)
