from django.urls import path
#from django.views.generic import TemplateView
from .views import AboutView, CourseListView, ManageCourseListView, CreateCourseView, DeleteCourseView

app_name = "course"

urlpatterns = [
    #path('about/', TemplateView.as_view(template_name="course/about.html")),
    path('about/', AboutView.as_view(), name="about"), 
    path('course-list/', CourseListView.as_view(), name="course_list"),
    path('manage-course/', ManageCourseListView.as_view(), name="manage_course"),
    path('create-course/', CreateCourseView.as_view(), name="create_course"),
    path('delete-course/<int:pk>/', DeleteCourseView.as_view(), name="delete_course"),
]