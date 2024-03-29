from django import forms
import re
from .models import *

class ContactForm(forms.Form):
	title = forms.CharField(max_length=150, label="Заголовок", widget=forms.TextInput(attrs={"class": "form-control"}))
	author = forms.CharField(max_length=150, label="Автор", widget=forms.TextInput(attrs={"class": "form-control"}))
	content = forms.CharField(label="Ваш відгук", required=False, widget=forms.Textarea(attrs={
			"class": "form-control",
		}))

	class Meta:
		model = Contact
		# fields = '__all__'
		fields = ['title', "author", 'content',]
		widgets = {
			"title": forms.TextInput(attrs={"class": "form-control"}),
			"author": forms.TextInput(attrs={"class": "form-control"}),
			"content": forms.Textarea(attrs={
				"class": "form-control",
				"row": 7,
			}),
		}

	def clean_title(self):
		title = self.cleaned_data['title']
		if re.match(r"\d", title):
			raise ValidationError("Назва не повинна починатися з цифри")
		return title