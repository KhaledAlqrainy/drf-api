from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


from .models import Post
# Create your tests here.


class PostModelTests(TestCase):

    @classmethod
    
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test',password='test123')
        test_user.save()

        test_post = Post.objects.create(
            author = test_user,
            name = "khaled",
            title = 'Title of Blog',
            body = 'content'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)

        self.assertEqual(str(post.author), 'test')
        self.assertEqual(post.title, 'Title of Blog')
        self.assertEqual(post.body, 'content')
        self.assertEqual(post.name, 'khaled')

