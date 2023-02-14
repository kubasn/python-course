MENU_PROMPT = "Enter 'b' to create blog, 'l' to list 'blogs', 'r' to read one, 'p' to create post or 'q' to quit."
from blog import Blog

POST_TEMPLATE = '''
    ---- {} ---- 
    {}
     '''


blogs = dict()

def menu():
    print_blogs()
    selection = input(MENU_PROMPT)

    while selection != 'q':
        if selection == 'b':
            create_blog()
        elif selection == 'l':
            list_blogs()
        elif selection == 'r':
            read_blog()
        elif selection == 'p':
            create_post()
        selection = input(MENU_PROMPT)



def print_blogs():
    
    for key,value in blogs.items():
        print('- {}'.format(value))


def create_blog():
    title = input('Input title of the blog')
    author = input('Input author of the blog')

    blogs[title] = Blog(title,author)

def list_blogs():
    pass

def read_blog():
    title = input('Enter the blog title you want to read')
    print_posts(blogs[title])

def print_posts(blog):

    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title,post.content))

def create_post():
    blog_name = input('Enter the name of blog where you want to insert a post')
    title = input('Put title for the post')
    content = input('Enter the content of your post')

    blogs[blog_name].create_post(title,content)


