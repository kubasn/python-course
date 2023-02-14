from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post

MENU_PROMPT = "Enter 'b' to create blog, 'l' to list 'blogs', 'r' to read one, 'p' to create post or 'q' to quit."
POST_TEMPLATE = '''
    ---- {} ---- 
    {}
     '''

class AppTest(TestCase):


    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect =('b','Test','Test author','q')
            app.menu()
            self.assertIsNotNone(app.blogs['Test'])









    def test_print_blogs(self):
        blog = Blog('Test','Test Author')
        app.blogs = {'Test':blog}
        # all you do with patch in this example you replace it with the mock_print
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            # You know that you called app.print_blogs() so you can
            # make assertions to test that expectation
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_menu_calls_print_blogs(self):
         with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()
                # mocked_input.assert_called_with(MENU_PROMPT)


    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(MENU_PROMPT)
    def test_create_blog(self):
        # every time it's called it will return Test
        # with patch('builtins.input',return_value='Test') as mocked_input:
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test','Test Author')
            app.create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))
    def test_read_blog(self):
        blog = Blog('Test','Test Author')
        app.blogs = {'Test':blog}

        with patch('builtins.input',return_value='Test') as mocked_input:
            with patch('app.print_posts') as mocked_print_posts:
               app.read_blog()

               mocked_print_posts.assert_called_with(blog)


    def test_print_posts(self):
        blog = Blog('Test','Test Author')
        blog.create_post('Test Post','Test Content')
        app.blogs = {'Test':blog}

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post title','Post content')
        expected = '''
    ---- Post title ---- 
    Post content
     '''
        with patch('builtins.print') as marked_print:
            app.print_post(post)
            marked_print.assert_called_with(expected)

    def test_create_post(self):
        blog = Blog('Test','Test Author')
        app.blogs = {'Test':blog}

        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ('Test', 'Post title', 'Post content')

            app.create_post()

            self.assertEqual(blog.posts[0].title, 'Post title')
            self.assertEqual(blog.posts[0].content, 'Post content')