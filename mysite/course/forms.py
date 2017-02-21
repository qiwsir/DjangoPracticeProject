from django import forms
from .models import Course

class CreateCourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ("title", "overview")
