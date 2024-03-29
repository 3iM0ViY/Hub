from django import template
from news_en.models import Category_en

register = template.Library()


@register.inclusion_tag("news_en/menu_tpl.html")
def show_menu_en(menu_class_en="menu_en"):
	categories_en = Category_en.objects.all()
	return {"categories_en": categories_en, "menu_class_en": menu_class_en}