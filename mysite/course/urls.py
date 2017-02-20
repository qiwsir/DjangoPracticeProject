from django.conf.urls import url
from django.views.generic import TemplateView

from .views import AboutView, CourseListView, ManageCourseListView, CreateCourseView

urlpatterns = [
    url(r'about/$', AboutView.as_view(), name="about"),
    url(r'course-list/$', CourseListView.as_view(), name="course_list"),
    url(r'manage-course/$', ManageCourseListView.as_view(), name="manage_course"),
    url(r'create-course/$', CreateCourseView.as_view(), name="create_course"),
]
