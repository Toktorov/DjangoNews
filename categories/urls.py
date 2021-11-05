from django.urls import path
from categories.views import category_view, category_detail


urlpatterns = [
    path('', category_view, name = 'category_index'),
    path('category/<int:id>', category_detail, name = 'category_detail')
]