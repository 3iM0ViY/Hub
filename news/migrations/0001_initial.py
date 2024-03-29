# Generated by Django 4.0.3 on 2022-03-28 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Назва категорії')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Назва тєгу')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок посту')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('author', models.CharField(blank=True, max_length=150, verbose_name='Автор')),
                ('content', models.TextField(blank=True, verbose_name='Вміст')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Створено коли')),
                ('published', models.BooleanField(default=True, verbose_name='Опублікувати')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='Пости', to='news.category', verbose_name='Категорія')),
                ('tags', models.ManyToManyField(blank=True, related_name='Пости', to='news.tag', verbose_name='Теги')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]