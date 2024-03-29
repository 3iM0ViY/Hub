from django.db import models
from django.urls import reverse

# Create your models here.
'''
Category
========
title, slug

Tag
========
title, slug

Post
========
title, slug, author, content, photo, 
published, created_at, category, tags
'''

class Category(models.Model):
	title = models.CharField(max_length=255, verbose_name="Назва категорії")
	slug = models.SlugField(max_length=255, verbose_name="URL", unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("category", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Категорія(ю)"
		verbose_name_plural = "Категорії"
		ordering = ["title"]

class Tag(models.Model):
	title = models.CharField(max_length=255, verbose_name="Назва тєгу")
	slug = models.SlugField(max_length=255, verbose_name="URL", unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("tag", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Тег(у)"
		verbose_name_plural = "Теги"
		ordering = ["title"]

class Post(models.Model):
	title = models.CharField(max_length=255, verbose_name="Заголовок публікації")
	slug = models.SlugField(max_length=255, verbose_name="URL", unique=True)
	author = models.CharField(max_length=150, verbose_name="Автор", blank=True)
	content = models.TextField(blank=True, verbose_name="Вміст")
	photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено коли")
	published = models.BooleanField(default=True, verbose_name="Опублікувати")
	views = models.IntegerField(default=0, verbose_name="Кількість переглядів")
	category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="Публікації", blank=True, verbose_name="Категорія")
	tags = models.ManyToManyField(Tag, blank=True, related_name="Публікації", verbose_name="Теги")
	short_story = models.BooleanField(default=False, verbose_name="Коротка новина")

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("single", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Публікація(ю)"
		verbose_name_plural = "Публікації"
		ordering = ["-created_at"]

class Contact(models.Model):
	title = models.CharField(max_length=255, verbose_name="Заголовок")
	author = models.CharField(max_length=150, verbose_name="Автор", blank=True)
	content = models.TextField(blank=True, verbose_name="Вміст")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено коли")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Форма(у) контакту"
		verbose_name_plural = "Форми контакту"
		ordering = ["-created_at"]









# from django.utils import timezone

# class Post(models.Model):
#     title = models.CharField(max_length=255, verbose_name="Заголовок публікації")
#     slug = models.SlugField(max_length=255, verbose_name="URL", unique=True)
#     author = models.CharField(max_length=150, verbose_name="Автор", blank=True)
#     content = models.TextField(blank=True, verbose_name="Вміст")
#     photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
#     created_at = models.DateTimeField(editable=False, verbose_name="Створено коли")
#     created_at_modified = models.DateTimeField(verbose_name="Ваша дата і час")
#     published = models.BooleanField(default=True, verbose_name="Опублікувати")
#     views = models.IntegerField(default=0, verbose_name="Кількість переглядів")
#     category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="Публікації", blank=True, verbose_name="Категорія")
#     tags = models.ManyToManyField(Tag, blank=True, related_name="Публікації", verbose_name="Теги")
#     short_story = models.BooleanField(default=False, verbose_name="Коротка новина")

#     def __str__(self):
#         return self.title

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created_at = timezone.now()
			# self.created_at_modified = timezone.now()
    #     return super(Post, self).save(*args, **kwargs)

    	# if not self.created_at_modified:
     #        self.created_at = timezone.now()
     #    return super(Post, self).save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse("single", kwargs={"slug": self.slug})

#     class Meta:
#         verbose_name = "Публікація(ю)"
#         verbose_name_plural = "Публікації"
#         ordering = ["-created_at"]


# {% if post.created_at_modified %}{{ post.created_at_modified }}{% else %}{{ post.created_at }}{% endif %}