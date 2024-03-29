from django.contrib import admin
from django.utils.safestring import mark_safe

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
from .models import *

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	form = PostAdminForm
	save_as = True
	save_on_top = True
	list_display = ("id", "title", "slug", 'category', "get_photo", "created_at", "short_story", "published")
	list_editable = ("title", "short_story", "published")
	list_display_links = ("id",)
	search_fields = ("title",)
	list_filter = ("category", "tags", "author", "short_story", "published",)
	readonly_fields = ("created_at", "get_photo",)
	fields = ("title", "slug", "author", 'category', "tags", "content", "photo", "get_photo", "created_at", "short_story", "published")

	def get_photo(self, obj):
		if obj.photo:
			return mark_safe(f'<img src="{obj.photo.url}" width="50">')
		return "-"

	get_photo.short_description = "Фото"

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

class ContactAdmin(admin.ModelAdmin):
	save_as = True
	save_on_top = True
	list_display = ("id", "title", "created_at", "author")
	search_fields = ("title", "author",)
	list_filter = ("author",)
	readonly_fields = ("title", "content", "created_at", "author")
	fields = ("title", "author", "content", "created_at",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)