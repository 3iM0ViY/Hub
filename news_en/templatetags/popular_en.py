from django import template
from news_en.models import Post_en

register = template.Library()


@register.inclusion_tag("news_en/popular.html")
def get_popular_en(cnt=4):
    posts_en = Post_en.objects.order_by("-views_en")[:cnt]
    return {"posts_en": posts_en}