from django.db import models
from common.models import CommonModel


# Create your models here.


class Course(CommonModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    faculty = models.ForeignKey(
        "faculty.Faculty",
        on_delete=models.CASCADE,
        related_name="courses_taught",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    def show_faculty(self):
        return f"{self.faculty}"


class Quiz(CommonModel):

    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="quizzes",
        null=True,
        blank=True,
    )
    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="student_quizzes",
        null=True,
        blank=True,
    )
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - Grade: {self.grade}"


class Assignment(CommonModel):

    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="assignments",
        null=True,
        blank=True,
    )
    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="student_assignments",
        null=True,
        blank=True,
    )
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - Grade: {self.grade}"


class Enrollment(CommonModel):
    student = models.ForeignKey(
        "students.student", on_delete=models.CASCADE, related_name="enrollments"
    )
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="enrolled_students"
    )

    class Meta:
        unique_together = (
            "student",
            "course",
        )  # Ensures a student can only be enrolled in the same course once

    def __str__(self):
        return f"{self.student.student_info} is enrolled in {self.course.name}"


class FacultyTeaching(CommonModel):
    faculty = models.ForeignKey(
        "faculty.Faculty",
        on_delete=models.CASCADE,
        related_name="faculty_teaching",
        null=True,
        blank=True,
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="courses_taught",
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = (
            "faculty",
            "course",
        )  # Ensures a faculty can only be assigned to the same course once

    def __str__(self):
        return f"{self.faculty.faculty_info} is teaching {self.course.name}"


class Announcement(CommonModel):
    faculty = models.ForeignKey(
        "faculty.Faculty", on_delete=models.CASCADE, related_name="announcements"
    )
    courses = models.ManyToManyField(
        "courses.Course", related_name="announcements", blank=True
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.faculty.user.username}"
