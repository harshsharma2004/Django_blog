from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Post


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect('loginn')  # use named URL instead of hardcoded
    return render(request, 'blog/signup.html')


def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('upassword')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid username or password'})

    return render(request, 'blog/login.html')


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


@login_required
def new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(title=title, content=content, author=request.user)
        return redirect('home')

    return render(request, 'blog/newpost.html')


@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/mypost.html', {'posts': posts})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    post.delete()
    return redirect('my_posts')


def signout(request):
    logout(request)
    return redirect('loginn')
