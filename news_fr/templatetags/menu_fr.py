from django import template
from news_fr.models import Category_fr

register = template.Library()


@register.inclusion_tag("news_fr/menu_tpl.html")
def show_menu_fr(menu_class_fr="menu_fr"):
	categories_fr = Category_fr.objects.all()
	return {"categories_fr": categories_fr, "menu_class_fr": menu_class_fr}