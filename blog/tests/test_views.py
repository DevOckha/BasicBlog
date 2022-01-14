from django.test import Client, TestCase
from django.urls import reverse
from blog.models import Post
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.author = User.objects.create(username='testuser', password='testpass')
        self.post = Post.objects.create(
             author = self.author,
             title = 'testpost',
             content = 'testcontent',
             subcontent = 'testsubcontent',
             active = True,
             featured = True,
             slug = 'testpost'
        )
        self.deatil_url = reverse('post', kwargs={'slug': self.post.slug})
        self.posts_url = reverse('posts')

    def test_post_home_GET(self):

        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertNotContains(response, 'i am not in index page')


    def test_post_detail_GET(self):
        response = self.client.get(self.deatil_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post.html')
        self.assertNotContains(response, 'i am not in detail page')

    def test_posts_page_GET(self):
        response = self.client.get(self.posts_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')
        self.assertNotContains(response, 'hi i am alexander cabanel')