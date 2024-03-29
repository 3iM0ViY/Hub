from django import template
from news.models import Tag

register = template.Library()


@register.inclusion_tag("news/tags.html")
def show_tags(menu_class="menu"):
	tags = Tag.objects.all()
	return {"tags": tags, "menu_class": menu_class}