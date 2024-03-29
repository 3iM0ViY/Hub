from django.urls import path
from .views import *

urlpatterns = [
	path("", Home.as_view(), name="home"),
	path("category/<str:slug>", GetCategory.as_view(), name="category"),
	path("tag/<str:slug>", GetTag.as_view(), name="tag"),
	path("single/<str:slug>", Single.as_view(), name="single"),
	path("about_us", about_us, name="about_us"),
	path("search", Search.as_view(), name="search"),
	path("contact", contact, name="contact"),

	# path("category/<str:slug>", NewsCategory.as_view(), name="category"),
	# path("news/<str:slug>", Single.as_view(), name="single"),
]