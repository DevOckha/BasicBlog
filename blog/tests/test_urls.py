from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import home, posts, post

class TestUrls(SimpleTestCase):


    def test_posts_url_is_resolves(self):
        url = reverse('posts')
        self.assertEqual(resolve(url).func, posts)

    
    def test_post_url_is_resolves(self):
        url = reverse('post' ,args=['same-slug'])
        self.assertEqual(resolve(url).func, post)
    
    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)