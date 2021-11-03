# Generated by Django 3.2.7 on 2021-11-03 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post', verbose_name='Картинки')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_image', to='post.post')),
            ],
            options={
                'verbose_name': 'Изображение поста',
                'verbose_name_plural': 'Изображении поста',
                'ordering': ('-id',),
            },
        ),
    ]