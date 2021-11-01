from django.shortcuts import render

# Create your views here.
from .models import Post


def post_view(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'post_list':post})