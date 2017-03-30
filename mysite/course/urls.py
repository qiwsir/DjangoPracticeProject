from django.conf.urls import url
from django.views.generic import TemplateView

from .views import AboutView, CourseListView, ManageCourseListView, CreateCourseView, DeleteCourseView, CreateLessonView
from .views import ListLessonsView

urlpatterns = [
    url(r'about/$', AboutView.as_view(), name="about"),
    url(r'course-list/$', CourseListView.as_view(), name="course_list"),
    url(r'manage-course/$', ManageCourseListView.as_view(), name="manage_course"),
    url(r'create-course/$', CreateCourseView.as_view(), name="create_course"),
    url(r'delete-course/(?P<pk>\d+)/$', DeleteCourseView.as_view(), name="delete_course"),
    url(r'create-lesson/$', CreateLessonView.as_view(), name="create_lesson"),
    url(r'list-lessons/(?P<course_id>\d+)/$', ListLessonsView.as_view(), name="list_lessons"),
]
