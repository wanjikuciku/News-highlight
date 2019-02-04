import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''Class testing behaviours of the News class'''

    def setUp(self):
        '''method taht will run before every test case'''
        self.new_news = News('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com','https://abcnews.go.com','general','en','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()