from django.shortcuts import render
from .models import Post

def show_posts(request):
    posts = Post.objects.all()
    return render(request, 'playground/posts.html', {'posts': posts})