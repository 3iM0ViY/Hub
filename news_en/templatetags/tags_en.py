from django import template
from news_en.models import Tag_en

register = template.Library()


@register.inclusion_tag("news_en/tags.html")
def show_tags_en(menu_class_en="menu_en"):
	tags_en = Tag_en.objects.all()
	return {"tags_en": tags_en, "menu_class_en": menu_class_en}