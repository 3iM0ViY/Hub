from django.urls import path
from .views import *

urlpatterns = [
	path("", Home_fr.as_view(), name="home_fr"),
	path("category/<str:slug_fr>", GetCategory_fr.as_view(), name="category_fr"),
	path("tag/<str:slug_fr>", GetTag_fr.as_view(), name="tag_fr"),
	path("single/<str:slug_fr>", single_fr, name="single_fr"),
	path("about_us", about_us_fr, name="about_us_fr"),
	path("search", Search_fr.as_view(), name="search_fr"),
	path("contact", contact_fr, name="contact_fr"),
]