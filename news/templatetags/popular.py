from django import template
from news.models import Post

register = template.Library()


@register.inclusion_tag("news/popular.html")
def get_popular(cnt=4):
    posts = Post.objects.order_by("-views")[:cnt]
    return {"posts": posts}