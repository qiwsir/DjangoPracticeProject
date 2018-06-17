from django import forms
from django.core.files.base import ContentFile
from slugify import slugify
from urllib import request

from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')

    def clean_url(self):    #⑩
        url = self.cleaned_data['url']    #⑪
        valid_extensions = ['jpg', 'jpeg', 'png']    #⑫
        extension = url.rsplit('.', 1)[1].lower()    #⑬
        if extension not in valid_extensions:    #⑭
            raise forms.ValidationError("The given Url does not match valid image extension.")
        return url    #⑮

    def save(self, force_insert=False, force_update=False, commit=True):    #⑯
        image = super(ImageForm, self).save(commit=False)    #⑰
        image_url = self.cleaned_data['url']
        image_name = '{0}.{1}'.format(slugify(image.title), image_url.rsplit('.', 1)[1].lower())    
        response = request.urlopen(image_url)   #⑱
        image.image.save(image_name, ContentFile(response.read()), save=False)    #⑲
        if commit:
            image.save()

        return image
