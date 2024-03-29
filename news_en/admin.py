from django.contrib import admin
from django.utils.safestring import mark_safe

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
from .models import *

class Post_enAdminForm(forms.ModelForm):
    content_en = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post_en
        fields = '__all__'

class Post_enAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug_en": ("title_en",)}
	form = Post_enAdminForm
	save_as = True
	save_on_top = True
	list_display = ("id", "title_en", "slug_en", 'category_en', "get_photo_en", "created_at_en", "short_story_en", "published_en")
	list_editable = ("title_en", "short_story_en", "published_en")
	list_display_links = ("id",)
	search_fields = ("title_en",)
	list_filter = ("category_en", "tags_en", "author_en", "short_story_en", "published_en",)
	readonly_fields = ("created_at_en", "get_photo_en",)
	fields = ("title_en", "slug_en", "author_en", 'category_en', "tags_en", "content_en", "photo_en", "get_photo_en", "created_at_en", "short_story_en", "published_en")

	def get_photo_en(self, obj):
		if obj.photo_en:
			return mark_safe(f'<img src="{obj.photo_en.url}" width="50">')
		return "-"

	get_photo_en.short_description = "Фото"

class Category_enAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug_en": ("title_en",)}

class Tag_enAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug_en": ("title_en",)}

class Contact_enAdmin(admin.ModelAdmin):
	save_as = True
	save_on_top = True
	list_display = ("id", "title_en", "created_at_en", "author_en")
	search_fields = ("title_en", "author_en",)
	list_filter = ("author_en",)
	readonly_fields = ("title_en", "content_en", "created_at_en", "author_en")
	fields = ("title_en", "author_en", "content_en", "created_at_en",)

admin.site.register(Category_en, Category_enAdmin)
admin.site.register(Tag_en, Tag_enAdmin)
admin.site.register(Post_en, Post_enAdmin)
admin.site.register(Contact_en, Contact_enAdmin)