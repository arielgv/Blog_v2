from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView, ListView
from django.views.generic.detail import DetailView
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

def home(request):
    #Esta es la main view, recibe todos los post publicados por todos los usuarios, en orden desde el mas reciente
    #al más antiguo debajo. De ser actualizado (editado) el post, se prioriza la fecha Updated.
    context = {
        'posts' : Post.objects.all().order_by('-updated_at')
    }
    return render(request, 'blog/home.html', context)

def about(request):
    #Esta es una vista aún vacía, devuelve un html vacío.
    return render(request, 'blog/about.html', {'title':'About'})

class PostAPIView(APIView):
    #Esta vista de API maneja solicitudes del tipo POST para el modelo declarado. El metodo valida y 
    #deserializa los datos de la solicitud. Si la validacion tiene exito, se guarda el objeto.
    #En cualquier caso se devuelve una respuesta HTTP
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            # Guardar el objeto serializado
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(generics.ListCreateAPIView):
    # se crea una vista de lista para los objetos de Post que utiliza el Serializer
    # de Post. También se define el queryset para obtener
    # todos los objetos de Post.    
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    #Esta clase realiza comprobaciones de Login y acredita al usuario antes de permitirle
    #realizar cualquier cambio a un post
    model = Post
    fields = ['title', 'content']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('profile')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    def form_valid(self, form):
        form.instance.updated_at = timezone.now()
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    #Al igual que el módulo update , realiza distintas comprobaciones y validaciones
    #antes de permitirle al usuario poder Borrar el post.
    model = Post
    success_url = reverse_lazy('profile')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class SearchResultsView(ListView):
    #Esta clase devuelve el listado de búsqueda que se haya realizado en el recuadro de búsqueda que 
    #forma parte del frontend de la página.
    model = Post
    template_name = 'blog/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list
    
class PostDetailView(DetailView):
    model = Post


class UserPostsView(ListView):
    #Esta clase responde al recuadro de post particulares de un usuario. Visible desde el endpoint Profile
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-date_posted')
