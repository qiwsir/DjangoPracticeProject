from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from django.contrib.auth.models import User

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

class UserCourseMixin(UserMixin):
    model = Course


class ManageCourseListView(UserCourseMixin, ListView):
    template_name = 'course/manage_course_list.html'
    
