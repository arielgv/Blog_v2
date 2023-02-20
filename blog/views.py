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
    #This is the main view, it receives all posts published by all users, in order from the most recent
    #to oldest below. If the post is updated (edited), the Updated date is prioritized.
    context = {
        'posts' : Post.objects.all().order_by('-updated_at')
    }
    return render(request, 'blog/home.html', context)

def about(request):
    #This is still an empty view, it returns empty html.
    return render(request, 'blog/about.html', {'title':'About'})

class PostAPIView(APIView):
    #This API view handles POST requests to the declared model. The method validates and
    #deserialize the request data. If the validation succeeds, the object is saved.
    #In either case an HTTP response is returned
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            # Guardar el objeto serializado
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(generics.ListCreateAPIView):
    # create a list view for the Post objects used by the Serializer
    # of Post. Also define the queryset to get
    # all Post objects.   
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # This class performs login checks and accredits the user before allowing them
    # make any changes to a post
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
    #Like the update module, performs various checks and validations
    #before allowing the user to Delete the post.
    model = Post
    success_url = reverse_lazy('profile')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class SearchResultsView(ListView):
    # This class returns the search listing that has been performed in the search box that
    # is part of the frontend of the page.
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
    # This class responds to a user's particular post box. Visible from endpoint Profile
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-date_posted')
