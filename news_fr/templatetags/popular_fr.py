from django import template
from news_fr.models import Post_fr

register = template.Library()


@register.inclusion_tag("news_fr/popular.html")
def get_popular_fr(cnt=4):
    posts_fr = Post_fr.objects.order_by("-views_fr")[:cnt]
    return {"posts_fr": posts_fr}