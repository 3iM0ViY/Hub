from django import template
from news_fr.models import Tag_fr

register = template.Library()


@register.inclusion_tag("news_fr/tags.html")
def show_tags_fr(menu_class_fr="menu_fr"):
	tags_fr = Tag_fr.objects.all()
	return {"tags_fr": tags_fr, "menu_class_fr": menu_class_fr}