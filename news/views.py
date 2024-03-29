from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *
from django.db.models import F

class Home(ListView):
	model = Post
	template_name = "news/index.html"
	context_object_name = "posts"
	paginate_by = 2

	def get_context_data(self, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Ukrainian Civil Society Hub"
		return context

	def get_queryset(self):
		return Post.objects.filter(published=True)

class GetCategory(ListView):
	template_name = "news/category.html"
	context_object_name = "posts"
	allow_empty = False
	paginate_by = 2

	def get_context_data(self, *, object_list=None, **kwards):
		context = super().get_context_data(**kwards)
		context["title"] = Category.objects.get(slug=self.kwargs["slug"])
		return context

	def get_queryset(self):
		return Post.objects.filter(category__slug=self.kwargs["slug"], published=True)

class GetTag(ListView):
	template_name = "news/category.html"
	context_object_name = "posts"
	allow_empty = False
	paginate_by = 2

	def get_context_data(self, *, object_list=None, **kwards):
		context = super().get_context_data(**kwards)
		context["title"] = Tag.objects.get(slug=self.kwargs["slug"])
		return context

	def get_queryset(self):
		return Post.objects.filter(tags__slug=self.kwargs["slug"], published=True)

class Single(DetailView):
	model = Post
	context_object_name = "post"
	template_name = "news/single.html"

	def get_context_data(self, *, object_list=None, **kwards):
		context = super().get_context_data(**kwards)
		self.object.views = F("views") + 1
		self.object.save()
		self.object.refresh_from_db()
		return context

def about_us(request):
	return render(request, "news/about_us.html")

class Search(ListView):
	template_name = "news/search.html"
	context_object_name = "posts"
	paginate_by = 2

	def get_queryset(self):
		return Post.objects.filter(title__icontains=self.request.GET.get('s'), published=True)

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

def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			Contact.objects.create(**form.cleaned_data)
			return redirect("contact")
		# 	messages.success(request, "Вы успешно авторизовались!")
		# else:
		# 	messages.error(request, "Ошибка авторизации")
	else:
		# form = UserCreationForm()
		form = ContactForm()

	context = {
		"form": form,
	}
	return render(request, "news/contact.html", context)
