from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User



class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpass')
        self.post = Post.objects.create(
             author = self.user,
             title = 'testpost 1',
             content = 'testcontent',
             subcontent = 'testsubcontent',
             active = True,
             featured = True,
             slug = 'testpost'
        )
    

    def test_post_is_assigned_slug_on_creation(self):
        self.assertEqual(self.post.slug, 'testpost-1')
    

    