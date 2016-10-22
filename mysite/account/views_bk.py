from django.shortcuts import render
from .forms import UserForm, UserProfileForm

from django.http import HttpResponse

def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, prefix='user')
        userprofile_form = UserProfileForm(request.POST, prefix='userprofile')
        if user_form.is_valid() * userprofile_form.is_valid():
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password'])
            userprofile = userprofile_form.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return HttpResponse("good. you have registration successuflly.")
    else:
        user_form = UserForm()
        userprofile_form = UserProfileForm()
    return render(request, "account/register.html", {"user_form": user_form, "userprofile_form": userprofile_form})
            
