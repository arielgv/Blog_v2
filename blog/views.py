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
    context = {
        'posts' : Post.objects.all().order_by('-updated_at')
    }
    return render(request, 'blog/home.html', context)

def about(request):
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
    model = Post
    success_url = reverse_lazy('profile')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class SearchResultsView(ListView):
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
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-date_posted')
