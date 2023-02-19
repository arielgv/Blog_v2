from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Post
from blog.forms import PostForm


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