from django.urls import path
from .views import *

urlpatterns = [
	path("", Home_en.as_view(), name="home_en"),
	path("category/<str:slug_en>", GetCategory_en.as_view(), name="category_en"),
	path("tag/<str:slug_en>", GetTag_en.as_view(), name="tag_en"),
	path("single/<str:slug_en>", single_en, name="single_en"),
	path("about_us", about_us_en, name="about_us_en"),
	path("search", Search_en.as_view(), name="search_en"),
	path("contact", contact_en, name="contact_en"),
]