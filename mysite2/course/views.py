from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.shortcuts import redirect
from django.http import HttpResponse

import json

from .models import Course
from .forms import CreateCourseForm

from braces.views import LoginRequiredMixin

class AboutView(TemplateView):
    template_name = "course/about.html"


class CourseListView(ListView):    #③
    model = Course    #④
    context_object_name = "courses"    #⑤
    template_name = 'course/course_list.html'    #⑥


class UserMixin:    #①
    def get_queryset(self):
        qs = super(UserMixin, self).get_queryset()
        return qs.filter(user=self.request.user)

class UserCourseMixin(UserMixin, LoginRequiredMixin):    #②
    model = Course
    login_url = "/account/login/"

class ManageCourseListView(UserCourseMixin, ListView):    #③
    context_object_name = "courses"
    template_name = 'course/manage/manage_course_list.html'

class CreateCourseView(UserCourseMixin, CreateView):    #①
    fields = ['title', 'overview']     #②
    template_name = 'course/manage/create_course.html'

    def post(self, request, *args, **kargs):    #③
        form = CreateCourseForm(data=request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.user = self.request.user
            new_course.save()
            return redirect("course:manage_course")    #④
        return self.render_to_response({"form":form})    #⑤

class DeleteCourseView(UserCourseMixin, DeleteView):    #①
    #template_name = 'course/manage/delete_course_confirm.html'
    success_url = reverse_lazy("course:manage_course")

    def dispatch(self, *args, **kwargs):    #③
        resp = super(DeleteCourseView, self).dispatch(*args, **kwargs)    #④
        if self.request.is_ajax():    #⑤
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            return resp
