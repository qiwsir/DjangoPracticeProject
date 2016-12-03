from django.contrib import admin
from .models import UserProfile, UserInfo

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone')
    list_filter = ("phone",)

class UserInfoAdmin(admin.ModelAdmin):
	list_display = ("user", 'school', 'company', 'profession', 'address', 'aboutme', 'photo')
	list_filter = ("school", "company", "profession")
		
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserInfo, UserInfoAdmin)

