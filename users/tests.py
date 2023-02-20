from django.test import TestCase

from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from blog.models import Post

class UserPostsTestCase(APITestCase):
    # This test case is particular to DRF , APITestCase in this case generates two different users and
    # test each one in different cases to generate Posts.
    client = APIClient()

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', email='user1@example.com', password='testpassword')
        self.user2 = User.objects.create_user(
            username='user2', email='user2@example.com', password='testpassword')
        self.post1 = Post.objects.create(user=self.user1, title='Test post 1', content='Test post 1 content')
        self.post2 = Post.objects.create(user=self.user1, title='Test post 2', content='Test post 2 content')
        self.post3 = Post.objects.create(user=self.user2, title='Test post 3', content='Test post 3 content')

    def test_get_user_posts(self):
        
        url = reverse('user-posts', kwargs={'user_id': self.user1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['posts']), 2)

