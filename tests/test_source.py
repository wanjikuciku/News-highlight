import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''Class testing behaviours of the Source class'''

    def setUp(self):
        '''method taht will run before every test case'''
        self.new_source = Source('123','citizen news','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()