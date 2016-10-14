from django.shortcuts import render
from .forms import UserForm, UserProfileForm

def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, prefix='user')
        userprofile_form = UserProfileForm(request.POST, prefix='userprofile')
        if user_form.is_valid() * userprofile_form.is_valid():
            user = user_form.save()
            userprofile = userprofile_form.save(commit=False)
            userprofile.user = user
            userprofile.save()
            
