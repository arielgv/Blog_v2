from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from blog.models import Post
from blog.forms import PostForm
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer


#la clase ProfileList hereda de generics.ListCreateAPIView. 
# Esto proporciona una lista paginada de todos los perfiles 
# y permite la creación de nuevos perfiles a través del método HTTP POST.
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created. You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method=="GET":
        context = {
            'posts' : Post.objects.all()
        }
        return render(request, 'users/profile.html',context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_posted = timezone.now()
            post.save()
            return redirect('profile')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})