from django import forms
from django.contrib.auth.models import User
from .models import ArticleColumn

class ArticleColumnForm(forms.ModelForm):
	class Meta:
		model = ArticleColumn
		fields = ("column",)