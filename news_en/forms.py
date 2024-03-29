from django import forms
import re
from .models import *

class ContactForm_en(forms.Form):
	title_en = forms.CharField(max_length=150, label="Heading", widget=forms.TextInput(attrs={"class": "form-control"}))
	author_en = forms.CharField(max_length=150, label="Author", widget=forms.TextInput(attrs={"class": "form-control"}))
	content_en = forms.CharField(label="Your feedback", required=False, widget=forms.Textarea(attrs={
			"class": "form-control",
		}))

	class Meta:
		model = Contact_en
		# fields = '__all__'
		fields = ['title_en', "author_en", 'content_en',]
		widgets = {
			"title_en": forms.TextInput(attrs={"class": "form-control"}),
			"author_en": forms.TextInput(attrs={"class": "form-control"}),
			"content_en": forms.Textarea(attrs={
				"class": "form-control",
				"row": 7,
			}),
		}

	def clean_title(self):
		title_en = self.cleaned_data['title_en']
		if re.match(r"\d", title_en):
			raise ValidationError("Назва не повинна починатися з цифри")
		return title_en