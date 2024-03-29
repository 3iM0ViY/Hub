from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *
from django.db.models import F

class Home_en(ListView):
	model = Post_en
	template_name = "news_en/index.html"
	context_object_name = "posts_en"
	paginate_by = 2

	def get_context_data(self, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title_en"] = "Ukrainian Civil Society Hub"
		return context

	def get_queryset(self):
		return Post_en.objects.filter(published_en=True)

class GetCategory_en(ListView):
	template_name = "news_en/category.html"
	context_object_name = "posts_en"
	allow_empty = False
	paginate_by = 2

	def get_context_data(self, *, object_list=None, **kwards):
		context = super().get_context_data(**kwards)
		context["title_en"] = Category_en.objects.get(slug_en=self.kwargs["slug_en"])
		return context

	def get_queryset(self):
		return Post_en.objects.filter(category_en__slug_en=self.kwargs["slug_en"], published_en=True)

class GetTag_en(ListView):
	template_name = "news_en/category.html"
	context_object_name = "posts_en"
	allow_empty = False
	paginate_by = 2

	def get_context_data(self, *, object_list=None, **kwards):
		context = super().get_context_data(**kwards)
		context["title_en"] = Tag_en.objects.get(slug_en=self.kwargs["slug_en"])
		return context

	def get_queryset(self):
		return Post_en.objects.filter(tags_en__slug_en=self.kwargs["slug_en"], published_en=True)

def single_en(request, slug_en):
	# news_item = News.objects.get(pk=news_id)
	post_en = get_object_or_404(Post_en, slug_en=slug_en)
	post_en.views_en = F("views_en") + 1
	post_en.save()
	post_en.refresh_from_db()
	context = {
		'post_en': post_en,
	}
	return render(request, "news_en/single.html", context)

class Single_en(DetailView):
	model = Post_en
	context_object_name = "post_en"
	template_name = "news_en/single.html"

	def get_context_data(self, *, object_list=None, **kwards):
		context = super().get_context_data(**kwards)
		self.object.views_en = F("views_en") + 1
		self.object.save()
		self.object.refresh_from_db()
		return context

def about_us_en(request):
	return render(request, "news_en/about_us.html")

class Search_en(ListView):
	template_name = "news_en/search.html"
	context_object_name = "posts_en"
	paginate_by = 2

	def get_queryset(self):
		return Post_en.objects.filter(title_en__icontains=self.request.GET.get('s'), published_en=True)

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

def contact_en(request):
	if request.method == "POST":
		form_en = ContactForm_en(request.POST)
		if form_en.is_valid():
			Contact_en.objects.create(**form_en.cleaned_data)
			return redirect("contact_en")
		# 	messages.success(request, "Вы успешно авторизовались!")
		# else:
		# 	messages.error(request, "Ошибка авторизации")
	else:
		# form = UserCreationForm()
		form_en = ContactForm_en()

	context = {
		"form_en": form_en,
	}
	return render(request, "news_en/contact.html", context)
