from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class Category(models.Model):
    title = CharField(
        max_length=100, 
        verbose_name = "Название"
    )

    description = TextField(
        verbose_name = "Описание"
    )

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('-created', )