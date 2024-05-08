from django.urls import path
from . import views
from .views import (
    FacultyCoursesView,
    AddCourseContentView,
    CourseStudentsView,
    AddAssignmentView,
    CourseGradesView,
    AnnouncementView,
)

urlpatterns = [
    path("courses/", FacultyCoursesView.as_view()),
    path("courses/<int:courseId>/content/", AddCourseContentView.as_view()),
    path("courses/<int:courseId>/students/", CourseStudentsView.as_view()),
    path(
        "courses/<int:courseId>/assignments/",
        AddAssignmentView.as_view(),
        name="add-assignment",
    ),
    path(
        "courses/<int:courseId>/grades/",
        CourseGradesView.as_view(),
        name="course-grades",
    ),
    path(
        "courses/<int:courseId>/announcements/",
        AnnouncementView.as_view(),
        name="course-announcements",
    ),
]
