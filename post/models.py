from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name = "название", max_length=120)
    description = models.TextField(verbose_name = "описание")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "Посты"