from django.urls import path
from . import views
from .views import EnrolledCoursesView, CourseContentView, StudentCourseGradesView


urlpatterns = [
    path("", views.StudentsView.as_view()),
    path("<int:pk>/", views.StudentDetailView.as_view()),
    path("courses/", EnrolledCoursesView.as_view(), name="student-courses"),
    path(
        "courses/<int:courseId>/content/",
        CourseContentView.as_view(),
        name="course-content",
    ),
    path(
        "courses/<int:courseId>/grades/",
        StudentCourseGradesView.as_view(),
        name="course-grades",
    ),
]
