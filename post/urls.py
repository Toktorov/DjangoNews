from django.urls import path
from post.views import post_view, post_detail


urlpatterns = [
    path('', post_view, name = 'post_index'),
    path('news/<int:id>', post_detail, name = 'post_detail')
]