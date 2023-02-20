from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse

class PostModelTest(TestCase):
    #se crean tres métodos de prueba:   
    #test_title_content: este método verifica que el título y el contenido del post creado sean los esperados.
    #test_post_list_view: este método verifica que la lista de posts se carga correctamente,
    #el status code es 200, y se encuentra la cadena 'Test content' en la respuesta, 
    #además de que el template utilizado es 'blog/post_list.html'.
    #test_post_detail_view: este método verifica que la vista de detalle de un post se carga correctamente,
    #el status code es 200, y se encuentra la cadena 'Test Post' en la respuesta, además de 
    #que el template utilizado es 'blog/post_detail.html'. También se verifica que se obtiene 
    #un error 404 cuando se intenta acceder a un post inexistente.    
    #Cada método de prueba se ejecutará automáticamente cuando se ejecute la prueba. 
    #se puede ejecutar la prueba mediante el comando python manage.py test.

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