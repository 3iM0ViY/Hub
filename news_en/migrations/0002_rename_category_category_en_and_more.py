# Generated by Django 4.0.3 on 2022-04-01 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_en', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Category_en',
        ),
        migrations.RenameModel(
            old_name='Contact',
            new_name='Contact_en',
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='Post_en',
        ),
        migrations.RenameModel(
            old_name='Tag',
            new_name='Tag_en',
        ),
        migrations.AlterModelOptions(
            name='category_en',
            options={'ordering': ['title_en'], 'verbose_name': 'Категорія(ю)', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='contact_en',
            options={'ordering': ['-created_at_en'], 'verbose_name': 'Форма(у) контакту', 'verbose_name_plural': 'Форми контакту'},
        ),
        migrations.AlterModelOptions(
            name='post_en',
            options={'ordering': ['-created_at_en'], 'verbose_name': 'Публікація(ю)', 'verbose_name_plural': 'Публікації'},
        ),
        migrations.AlterModelOptions(
            name='tag_en',
            options={'ordering': ['title_en'], 'verbose_name': 'Тег(у)', 'verbose_name_plural': 'Теги'},
        ),
        migrations.RenameField(
            model_name='category_en',
            old_name='slug',
            new_name='slug_en',
        ),
        migrations.RenameField(
            model_name='category_en',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='contact_en',
            old_name='author',
            new_name='author_en',
        ),
        migrations.RenameField(
            model_name='contact_en',
            old_name='content',
            new_name='content_en',
        ),
        migrations.RenameField(
            model_name='contact_en',
            old_name='created_at',
            new_name='created_at_en',
        ),
        migrations.RenameField(
            model_name='contact_en',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='post_en',
            old_name='author',
            new_name='author_en',
        ),
        migrations.RenameField(
            model_name='post_en',
            old_name='category',
            new_name='category_en',
        ),
        migrations.RenameField(
            model_name='post_en',
            old_name='content',
            new_name='content_en',
        ),
        migrations.RenameField(
            model_name='post_en',
            old_name='created_at',
            new_name='created_at_en',
        ),
        migrations.RenameField(
            model_name='post_en',
            old_name='photo',
            new_name='photo_en',
        ),
        migrations.RenameField(
            model_name='post_en',
            old_name='published',
            new_name='published_en',
        ),
        migrations.RenameField(
            model_name='post_en',
            old_name='short_story',
            new_name='short_story_en',
        ),
        migrations.RenameField(
            model_name='post_en',
            old_name='slug',
            new_name='slug_en',
        ),
        migrations.RenameField(
            model_name='post_en',
            old_name='tags',
            new_name='tags_en',
        ),
        migrations.RenameField(
            model_name='post_en',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='post_en',
            old_name='views',
            new_name='views_en',
        ),
        migrations.RenameField(
            model_name='tag_en',
            old_name='slug',
            new_name='slug_en',
        ),
        migrations.RenameField(
            model_name='tag_en',
            old_name='title',
            new_name='title_en',
        ),
    ]