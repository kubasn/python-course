import unittest
from blog import Blog


class BlogTest(unittest.TestCase):
    def test_create_blog(self):
        b = Blog('Cooking recipes','Tom')
    
        self.assertEqual('Cooking recipes', b.title)
        self.assertEqual('Tom', b.author)
        self.assertListEqual([], b.posts)

    def test__repr__(self):
        b = Blog('Test','Test Author')

        b2= Blog('Test2','Test Author2')

        self.assertEqual(b.__repr__(),'Test by Test Author (0 posts)')
        
        self.assertEqual(b2.__repr__(),'Test2 by Test Author2 (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test','Test Author')
        b.posts = ['test']

        self.assertEqual(b.__repr__(),'Test by Test Author (1 post)')

        b.posts = ['test','awd']
        
        self.assertEqual(b.__repr__(),'Test by Test Author (2 posts)')




# tdd - test driven development - thing of what you gonna implement before implementing it
# 