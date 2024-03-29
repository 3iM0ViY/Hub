from django.contrib import admin
from django.utils.safestring import mark_safe

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
from .models import *

class Post_frAdminForm(forms.ModelForm):
    content_fr = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post_fr
        fields = '__all__'

class Post_frAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug_fr": ("title_fr",)}
	form = Post_frAdminForm
	save_as = True
	save_on_top = True
	list_display = ("id", "title_fr", "slug_fr", 'category_fr', "get_photo_fr", "created_at_fr", "short_story_fr", "published_fr")
	list_editable = ("title_fr", "short_story_fr", "published_fr")
	list_display_links = ("id",)
	search_fields = ("title_fr",)
	list_filter = ("category_fr", "tags_fr", "author_fr", "short_story_fr", "published_fr",)
	readonly_fields = ("created_at_fr", "get_photo_fr",)
	fields = ("title_fr", "slug_fr", "author_fr", 'category_fr', "tags_fr", "content_fr", "photo_fr", "get_photo_fr", "created_at_fr", "short_story_fr", "published_fr")

	def get_photo_fr(self, obj):
		if obj.photo_fr:
			return mark_safe(f'<img src="{obj.photo_fr.url}" width="50">')
		return "-"

	get_photo_fr.short_description = "Фото"

class Category_frAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug_fr": ("title_fr",)}

class Tag_frAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug_fr": ("title_fr",)}

class Contact_frAdmin(admin.ModelAdmin):
	save_as = True
	save_on_top = True
	list_display = ("id", "title_fr", "created_at_fr", "author_fr")
	search_fields = ("title_fr", "author_fr",)
	list_filter = ("author_fr",)
	readonly_fields = ("title_fr", "content_fr", "created_at_fr", "author_fr")
	fields = ("title_fr", "author_fr", "content_fr", "created_at_fr",)

admin.site.register(Category_fr, Category_frAdmin)
admin.site.register(Tag_fr, Tag_frAdmin)
admin.site.register(Post_fr, Post_frAdmin)
admin.site.register(Contact_fr, Contact_frAdmin)