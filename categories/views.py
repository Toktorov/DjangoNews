from django.shortcuts import render
from categories.models import Category

# Create your views here.
def category_view(request):
    category = Category.objects.all()
    return render(request, 'category/index.html', {'category':category})

def category_detail(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'category/detail.html', {'category' : category})