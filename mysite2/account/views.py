from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login    #①
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo
from .forms import LoginForm, RegistrationForm, UserProfileForm

def user_login(request):    #②
    if request.method == "POST":    #③
        login_form = LoginForm(request.POST)    #④
        if login_form.is_valid():    #⑤
            cd = login_form.cleaned_data    #⑥
            user = authenticate(username=cd['username'], password=cd['password'])    #⑦
            if user:
                login(request, user)    #⑧
                return HttpResponse("Wellcome You. You have been authenticated successfully")    #⑨
            else:
                return HttpResponse("Sorry. Your username or password is not right.")
        else:
            return HttpResponse("Invalid login")
    
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})

# def register(request):
#     if request.method == "POST":
#         user_form = RegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)    #①
#             new_user.set_password(user_form.cleaned_data['password'])    #②
#             new_user.save()
#             return HttpResponse("successfully")
#         else:
#             return HttpResponse("sorry, your can not register.")
#     else:
#         user_form = RegistrationForm()
#         return render(request, "account/register.html", {"form": user_form})

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)
            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry, your can not register.")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {"form": user_form, "profile":userprofile_form})

@login_required(login_url='/account/login/')    #②
def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request, "account/myself.html", {"user":user, "userinfo":userinfo, "userprofile":userprofile})
