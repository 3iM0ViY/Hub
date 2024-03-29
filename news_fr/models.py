from django.db import models
from django.urls import reverse

class Category_fr(models.Model):
	title_fr = models.CharField(max_length=255, verbose_name="Назва категорії")
	slug_fr = models.SlugField(max_length=255, verbose_name="URL", unique=True)

	def __str__(self):
		return self.title_fr

	def get_absolute_url_fr(self):
		return reverse("category_fr", kwargs={"slug_fr": self.slug_fr})

	class Meta:
		verbose_name = "Категорія(ю)"
		verbose_name_plural = "Категорії"
		ordering = ["title_fr"]

class Tag_fr(models.Model):
	title_fr = models.CharField(max_length=255, verbose_name="Назва тєгу")
	slug_fr = models.SlugField(max_length=255, verbose_name="URL", unique=True)

	def __str__(self):
		return self.title_fr

	def get_absolute_url_fr(self):
		return reverse("tag_fr", kwargs={"slug_fr": self.slug_fr})

	class Meta:
		verbose_name = "Тег(у)"
		verbose_name_plural = "Теги"
		ordering = ["title_fr"]

class Post_fr(models.Model):
	title_fr = models.CharField(max_length=255, verbose_name="Заголовок публікації")
	slug_fr = models.SlugField(max_length=255, verbose_name="URL", unique=True)
	author_fr = models.CharField(max_length=150, verbose_name="Автор", blank=True)
	content_fr = models.TextField(blank=True, verbose_name="Вміст")
	photo_fr = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
	created_at_fr = models.DateTimeField(auto_now_add=True, verbose_name="Створено коли")
	published_fr = models.BooleanField(default=True, verbose_name="Опублікувати")
	views_fr = models.IntegerField(default=0, verbose_name="Кількість переглядів")
	category_fr = models.ForeignKey(Category_fr, on_delete=models.PROTECT, related_name="Публікації", blank=True, verbose_name="Категорія")
	tags_fr = models.ManyToManyField(Tag_fr, blank=True, related_name="Публікації", verbose_name="Теги")
	short_story_fr = models.BooleanField(default=False, verbose_name="Коротка новина")

	def __str__(self):
		return self.title_fr
	
	def get_absolute_url_fr(self):
		return reverse("single_fr", kwargs={"slug_fr": self.slug_fr})

	class Meta:
		verbose_name = "Публікація(ю)"
		verbose_name_plural = "Публікації"
		ordering = ["-created_at_fr"]

class Contact_fr(models.Model):
	title_fr = models.CharField(max_length=255, verbose_name="Заголовок")
	author_fr = models.CharField(max_length=150, verbose_name="Автор", blank=True)
	content_fr = models.TextField(blank=True, verbose_name="Вміст")
	created_at_fr = models.DateTimeField(auto_now_add=True, verbose_name="Створено коли")

	def __str__(self):
		return self.title_fr

	class Meta:
		verbose_name = "Форма(у) контакту"
		verbose_name_plural = "Форми контакту"
		ordering = ["-created_at_fr"]