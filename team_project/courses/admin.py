from django.contrib import admin
from .models import (
    Course,
    Assignment,
    Quiz,
    Enrollment,
    FacultyTeaching,
)

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "show_faculty",  # "faculty",
        "description",
        "is_published",
    )


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
    )


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course")


@admin.register(FacultyTeaching)
class FacultyTeachingAdmin(admin.ModelAdmin):
    list_display = ("faculty", "course")
