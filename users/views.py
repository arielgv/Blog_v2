from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.models import Post
from blog.forms import PostForm
from rest_framework import generics, status
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
from .serializers import ProfileSerializer


# The ProfileList class inherits from generics.ListCreateAPIView.
# This provides a paginated list of all profiles
# and allows the creation of new profiles via the HTTP POST method.
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
            'posts' : Post.objects.all().order_by('-updated_at')
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

# this is for Unity test: Users list

@csrf_exempt
def user_posts(request, user_id):
    # view based on function returning a list of all
    # a user's posts, their URL is /api/posts/<int:user_id>/
    if request.method == 'GET':
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        posts = user.posts.all()
        response_data = {'posts': list(posts.values())}
        return JsonResponse(response_data, status=status.HTTP_200_OK)
        
