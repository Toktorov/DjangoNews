from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


# Create your views here.
def post_view(request):
    post = Post.objects.all()
    return render(request, 'news/index.html', {'post':post})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'news/detail.html', {'post':post})