from django import forms
import re
from .models import *

class ContactForm_fr(forms.Form):
	title_fr = forms.CharField(max_length=150, label="Titre", widget=forms.TextInput(attrs={"class": "form-control"}))
	author_fr = forms.CharField(max_length=150, label="L'écrivain(e)", widget=forms.TextInput(attrs={"class": "form-control"}))
	content_fr = forms.CharField(label="Vos réactions", required=False, widget=forms.Textarea(attrs={
			"class": "form-control",
		}))

	class Meta:
		model = Contact_fr
		# fields = '__all__'
		fields = ['title_fr', "author_fr", 'content_fr',]
		widgets = {
			"title_fr": forms.TextInput(attrs={"class": "form-control"}),
			"author_fr": forms.TextInput(attrs={"class": "form-control"}),
			"content_fr": forms.Textarea(attrs={
				"class": "form-control",
				"row": 7,
			}),
		}

	def clean_title(self):
		title_fr = self.cleaned_data['title_fr']
		if re.match(r"\d", title_fr):
			raise ValidationError("Назва не повинна починатися з цифри")
		return title_fr