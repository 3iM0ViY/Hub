from django.db import models
from django.urls import reverse

class Category_en(models.Model):
	title_en = models.CharField(max_length=255, verbose_name="Назва категорії")
	slug_en = models.SlugField(max_length=255, verbose_name="URL", unique=True)

	def __str__(self):
		return self.title_en

	def get_absolute_url_en(self):
		return reverse("category_en", kwargs={"slug_en": self.slug_en})

	class Meta:
		verbose_name = "Категорія(ю)"
		verbose_name_plural = "Категорії"
		ordering = ["title_en"]

class Tag_en(models.Model):
	title_en = models.CharField(max_length=255, verbose_name="Назва тєгу")
	slug_en = models.SlugField(max_length=255, verbose_name="URL", unique=True)

	def __str__(self):
		return self.title_en

	def get_absolute_url_en(self):
		return reverse("tag_en", kwargs={"slug_en": self.slug_en})

	class Meta:
		verbose_name = "Тег(у)"
		verbose_name_plural = "Теги"
		ordering = ["title_en"]

class Post_en(models.Model):
	title_en = models.CharField(max_length=255, verbose_name="Заголовок публікації")
	slug_en = models.SlugField(max_length=255, verbose_name="URL", unique=True)
	author_en = models.CharField(max_length=150, verbose_name="Автор", blank=True)
	content_en = models.TextField(blank=True, verbose_name="Вміст")
	photo_en = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
	created_at_en = models.DateTimeField(auto_now_add=True, verbose_name="Створено коли")
	published_en = models.BooleanField(default=True, verbose_name="Опублікувати")
	views_en = models.IntegerField(default=0, verbose_name="Кількість переглядів")
	category_en = models.ForeignKey(Category_en, on_delete=models.PROTECT, related_name="Публікації", blank=True, verbose_name="Категорія")
	tags_en = models.ManyToManyField(Tag_en, blank=True, related_name="Публікації", verbose_name="Теги")
	short_story_en = models.BooleanField(default=False, verbose_name="Коротка новина")

	def __str__(self):
		return self.title_en
	
	def get_absolute_url_en(self):
		return reverse("single_en", kwargs={"slug_en": self.slug_en})

	class Meta:
		verbose_name = "Публікація(ю)"
		verbose_name_plural = "Публікації"
		ordering = ["-created_at_en"]

class Contact_en(models.Model):
	title_en = models.CharField(max_length=255, verbose_name="Заголовок")
	author_en = models.CharField(max_length=150, verbose_name="Автор", blank=True)
	content_en = models.TextField(blank=True, verbose_name="Вміст")
	created_at_en = models.DateTimeField(auto_now_add=True, verbose_name="Створено коли")

	def __str__(self):
		return self.title_en

	class Meta:
		verbose_name = "Форма(у) контакту"
		verbose_name_plural = "Форми контакту"
		ordering = ["-created_at_en"]