from django.conf.urls import url
from django.views.generic import TemplateView   
from .views import AboutView, CourseListView, ManageCourseListView, CreateCourseView, DeleteCourseView, CreateLessonView, ListLessonsView, DetailLessonView
from .views import StudentListLessonView

urlpatterns = [
    #url(r'about/$', TemplateView.as_view(template_name="course/about.html")),   
    url(r'about/$', AboutView.as_view(), name="about"),    
    url(r'course-list/$', CourseListView.as_view(), name="course_list"),
    url(r'manage-course/$', ManageCourseListView.as_view(), name="manage_course"),
    url(r'create-course/$', CreateCourseView.as_view(), name="create_course"),
    url(r'delete-course/(?P<pk>\d+)/$', DeleteCourseView.as_view(), name="delete_course"),
    url(r'create-lesson/$', CreateLessonView.as_view(), name="create_lesson"),
    url(r'list-lessons/(?P<course_id>\d+)/$', ListLessonsView.as_view(), name="list_lessons"),
    url(r'detail-lesson/(?P<lesson_id>\d+)/$', DetailLessonView.as_view(), name="detail_lesson"),
    url(r'lessons-list/(?P<course_id>\d+)/$', StudentListLessonView.as_view(), name="lessons_list"),
]


