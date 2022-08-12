from django.test import TestCase, LiveServerTestCase, Client
from django.test.testcases import skipIfDBFeature
from posts.models import Post
from posts import views
# Create your tests here.


class PostTestCase(LiveServerTestCase):
    # def setUp(self):
    #     title = 'new title'
    #     message = 'new message'
    #     self.data_dict = {'title':title, 'message':message}
    #     Post.objects.create(**self.data_dict)

    # @skipIfDBFeature('supports_transactions')
    # def test_posts_can_speak(self):
    #     """Posts that can speak are correctly identified"""
    #     new_title = Post.objects.get_queryset().first()
    #     # print(new_title.title, new_title.message)

    #     self.assertEqual(new_title.title, self.data_dict['title'])

    def test_posts_load(self):
        c = Client()
        response = c.get('/posts/')
        self.assertEqual(response.status_code, 200)
