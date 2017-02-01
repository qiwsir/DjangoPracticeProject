from django import forms

class HaySearchForm(forms.Form):
    query = forms.CharField()
