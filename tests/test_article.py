import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''Test class to test the beahviour of the Article class'''

    def setUp(self):
        '''method that will run before each test case'''
        self.new_article = Article('123',"Title of the article",'description of the article','https://abcnews.go.com/theview/video/andrea-kelly-details-allegations-abuse-husband-kelly-58286731','https://s.abcnews.com/images/theview/181004_view_andrea_1134_hpMain_16x9_992.jpg','2018-10-04T18:14:14Z','content of the article')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
    
    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id, '123')
        self.assertEquals(self.new_article.title, 'Title of the article')
        self.assertEquals(self.new_article.description, 'description of the article')
        self.assertEquals(self.new_article.url, 'https://abcnews.go.com/theview/video/andrea-kelly-details-allegations-abuse-husband-kelly-58286731')
        self.assertEquals(self.new_article.urlToImage, 'https://s.abcnews.com/images/theview/181004_view_andrea_1134_hpMain_16x9_992.jpg')
        self.assertEquals(self.new_article.publishedAt, '2018-10-04T18:14:14Z')
        self.assertEquals(self.new_article.content,'content of the article')

if __name__ == '__main__':
    unittest.main()