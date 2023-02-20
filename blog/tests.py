from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse

class PostModelTest(TestCase):
    # three test methods are created:
    #test_title_content: This method verifies that the title and content of the created post are as expected.
    #test_post_list_view: this method verifies that the list of posts is loaded correctly,
    #the status code is 200, and the string 'Test content' is found in the response,
    #besides that the template used is 'blog/post_list.html'.
    #test_post_detail_view: This method verifies that the detail view of a post is loaded correctly,
    #the status code is 200, and the string 'Test Post' is found in the response, plus
    #that the template used is 'blog/post_detail.html'. It is also verified that one obtains
    #a 404 error when trying to access a non-existent post.
    #Each test method will be executed automatically when the test is executed.
    #the test can be run using the python manage.py test command.

    @classmethod
    def setUpTestData(cls):
        # Crea un usuario para cada prueba
        testuser1 = User.objects.create_user(
            username='testuser1', password='testpass123')

        # Crea un post para cada prueba
        test_post = Post.objects.create(
            author=testuser1, title='Test Post', content='Test content')

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_content = f'{post.content}'
        self.assertEquals(expected_title, 'Test Post')
        self.assertEquals(expected_content, 'Test content')

    def test_post_list_view(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test content')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'blog/post_detail.html')