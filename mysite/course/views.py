from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy

from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User

from braces.views import LoginRequiredMixin

from .models import Course

class AboutView(TemplateView):
    template_name = "course/about.html"

class CourseListView(ListView):
    model = Course
    #queryset = Course.objects.filter(user=User.objects.filter(username="lulaoshi"))
    context_object_name = "courses"
    template_name = 'course/course_list.html'

    def get_queryset(self):
        qs = super(CourseListView, self).get_queryset()
        #return qs.filter(user=self.request.user)
        return qs.filter(user=User.objects.filter(username="lulaoshi"))


class UserMixin(object):
    def get_queryset(self):
        qs = super(UserMixin, self).get_queryset()
        return qs.filter(user=self.request.user)

class UserCourseMixin(UserMixin, LoginRequiredMixin):
    model = Course
    login_url = "/account/login/"

class ManageCourseListView(UserCourseMixin, ListView):
    template_name = 'course/manage/manage_course_list.html'
    context_object_name = "courses"

class CreateCourseView(UserCourseMixin, CreateView):
    fields = ['title', 'overview']
    template_name = 'course/manage/create_course.html'
    success_url = reverse_lazy("course:manage_course")
