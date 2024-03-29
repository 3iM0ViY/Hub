# Generated by Django 4.0.3 on 2022-03-29 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категорія(ю)', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title'], 'verbose_name': 'Публікація(ю)', 'verbose_name_plural': 'Публікації'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title'], 'verbose_name': 'Тег(у)', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddField(
            model_name='post',
            name='short_story',
            field=models.BooleanField(default=False, verbose_name='Коротка новина'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='Публікації', to='news.category', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='Публікації', to='news.tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок публікації'),
        ),
    ]