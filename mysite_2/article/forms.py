from django import forms
from .models import ArticleColumn, ArticlePost, Comment
from .models import ArticleTag

class ArticleColumnForm(forms.ModelForm): 
    class Meta:
        model = ArticleColumn 
        fields = ("column",)

class ArticlePostForm(forms.ModelForm): 
    class Meta:
        model = ArticlePost 
        fields = ("title", "body")


class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ("commentator", "body",)

class ArticleTagForm(forms.ModelForm):
    class Meta:
        model = ArticleTag 
        fields = ('tag', )