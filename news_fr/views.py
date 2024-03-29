from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *
from django.db.models import F

class Home_fr(ListView):
	model = Post_fr
	template_name = "news_fr/index.html"
	context_object_name = "posts_fr"
	paginate_by = 2

	def get_context_data(self, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title_fr"] = "Ukrainian Civil Society Hub"
		return context

	def get_queryset(self):
		return Post_fr.objects.filter(published_fr=True)

class GetCategory_fr(ListView):
	template_name = "news_fr/category.html"
	context_object_name = "posts_fr"
	allow_empty = False
	paginate_by = 2

	def get_context_data(self, *, object_list=None, **kwards):
		context = super().get_context_data(**kwards)
		context["title_fr"] = Category_fr.objects.get(slug_fr=self.kwargs["slug_fr"])
		return context

	def get_queryset(self):
		return Post_fr.objects.filter(category_fr__slug_fr=self.kwargs["slug_fr"], published_fr=True)

class GetTag_fr(ListView):
	template_name = "news_fr/category.html"
	context_object_name = "posts_fr"
	allow_empty = False
	paginate_by = 2

	def get_context_data(self, *, object_list=None, **kwards):
		context = super().get_context_data(**kwards)
		context["title_fr"] = Tag_fr.objects.get(slug_fr=self.kwargs["slug_fr"])
		return context

	def get_queryset(self):
		return Post_fr.objects.filter(tags_fr__slug_fr=self.kwargs["slug_fr"], published_fr=True)

def single_fr(request, slug_fr):
	# news_item = News.objects.get(pk=news_id)
	post_fr = get_object_or_404(Post_fr, slug_fr=slug_fr)
	post_fr.views_fr = F("views_fr") + 1
	post_fr.save()
	post_fr.refresh_from_db()
	context = {
		'post_fr': post_fr,
	}
	return render(request, "news_fr/single.html", context)

class Single_fr(DetailView):
	model = Post_fr
	context_object_name = "post_fr"
	template_name = "news_fr/single.html"

	def get_context_data(self, *, object_list=None, **kwards):
		context = super().get_context_data(**kwards)
		self.object.views_fr = F("views_fr") + 1
		self.object.save()
		self.object.refresh_from_db()
		return context

def about_us_fr(request):
	return render(request, "news_fr/about_us.html")

class Search_fr(ListView):
	template_name = "news_fr/search.html"
	context_object_name = "posts_fr"
	paginate_by = 2

	def get_queryset(self):
		return Post_fr.objects.filter(title_fr__icontains=self.request.GET.get('s'), published_fr=True)

	def get_context_data(self, *, object_list=None, **kwards):
		context = super().get_context_data(**kwards)
		context['s'] = f"s={self.request.GET.get('s')}&"
		return context

# class Contact(CreateView):
# 	model = Contact
# 	form_class = ContactForm
# 	template_name = "contact.html"
# 	#success_url = reverse_lazy("home")
# 	#raise_exception = True

# 	def get_context_data(self, *, object_list=None, **kwards):
# 		context = super().get_context_data(**kwards)
# 		return context

def contact_fr(request):
	if request.method == "POST":
		form_fr = ContactForm_fr(request.POST)
		if form_fr.is_valid():
			Contact_fr.objects.create(**form_fr.cleaned_data)
			return redirect("contact_fr")
		# 	messages.success(request, "Вы успешно авторизовались!")
		# else:
		# 	messages.error(request, "Ошибка авторизации")
	else:
		# form = UserCreationForm()
		form_fr = ContactForm_fr()

	context = {
		"form_fr": form_fr,
	}
	return render(request, "news_fr/contact.html", context)
