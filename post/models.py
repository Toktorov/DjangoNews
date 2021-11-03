from typing import ForwardRef
from django.db import models
from django.db.models.fields import related
from categories.models import Category

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        verbose_name = "название", 
        max_length=120
    )

    description = models.TextField(
        verbose_name = "описание"
    )

    category = models.ForeignKey(Category,
        related_name='post_category',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "Посты"
        ordering = ('-created', )

class PostImage(models.Model):
    image = models.ImageField(
        upload_to='post',
        verbose_name='Картинки',
        blank=True, null=True
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='post_image'
    )

    def __str__(self):
        return f"{self.post.id}"


    class Meta:
        verbose_name = 'Изображение поста'
        verbose_name_plural = 'Изображении поста'
        ordering = ('-id',)
