from django.contrib import admin
from .models import Faculty
from courses.models import Course

# Register your models here.


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = [
        "faculty_info",
        "department",
        "taught_courses",
    ]
