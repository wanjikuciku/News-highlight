import unittest
from app.models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = News('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com','general','en','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,News))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id, 'abc-news')
        self.assertEquals(self.new_source.name, 'ABC News')
        self.assertEquals(self.new_source.description, 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.')
        self.assertEquals(self.new_source.url, 'https://abcnews.go.com')
        self.assertEquals(self.new_source.category, 'general')
        self.assertEquals(self.new_source.language, 'en')
        self.assertEquals(self.new_source.country, 'us')
        
if __name__ == '__main__':
    unittest.main()