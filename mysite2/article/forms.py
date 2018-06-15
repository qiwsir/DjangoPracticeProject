from django import forms
from .models import ArticleColumn, ArticlePost

class ArticleColumnForm(forms.ModelForm):
	class Meta:
		model = ArticleColumn
		fields = ("column",)

class ArticlePostForm(forms.ModelForm):
	class Meta:
		model = ArticlePost
		fields = ("title", "body")
