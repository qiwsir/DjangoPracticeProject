from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.base import TemplateResponseMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views import View

import json

from .models import Course, Lesson
from .forms import CreateCourseForm, CreateLessonForm

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

class CreateLessonView(LoginRequiredMixin, View):    #②
    model = Lesson
    login_url = "/account/login/"

    def get(self, request , *args, **kwargs):    #③
        form = CreateLessonForm(user=self.request.user)    #④
        return render(request, "course/manage/create_lesson.html", {"form":form})

    def post(self, request, *args, **kwargs):    #⑤
        form = CreateLessonForm(self.request.user, request.POST, request.FILES)    #⑥
        if form.is_valid():
            new_lesson = form.save(commit=False)
            new_lesson.user = self.request.user
            new_lesson.save()
            return redirect("course:manage_course")

class ListLessonsView(LoginRequiredMixin, TemplateResponseMixin, View):    #②
    login_url = "/account/login/"
    template_name = 'course/manage/list_lessons.html'    #③

    def get(self, request, course_id):    #④
        course = get_object_or_404(Course, id=course_id)    #⑤
        return self.render_to_response({'course':course})    #⑥

class DetailLessonView(LoginRequiredMixin, TemplateResponseMixin, View):
    login_url = "/account/login/"
    template_name = "course/manage/detail_lesson.html"

    def get(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, id=lesson_id)
        return self.render_to_response({"lesson":lesson})

class StudentListLessonView(ListLessonsView):    #①
    template_name = "course/slist_lessons.html"    #②

    def post(self, request, *args, **kwargs):
        course = Course.objects.get(id=kwargs['course_id'])
        course.student.add(self.request.user)
        return HttpResponse("ok")
