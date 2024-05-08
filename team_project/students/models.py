from django.db import models
from common.models import CommonModel
from courses.models import Enrollment

# Create your models here.


class Student(CommonModel):
    student_info = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="student_profile"
    )
    student_id = models.PositiveBigIntegerField(unique=True, blank=True, null=True)
    notifications_enabled = models.BooleanField(default=False)
    major = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student_info} - {self.major}"

    def enrolled_courses(self):
        return self.enrollments.all()

    def get_quizzes_by_course(self, course_id):
        return self.student_quizzes.filter(course_id=course_id).all()

    def get_assignments_by_course(self, course_id):
        return self.student_assignments.filter(course_id=course_id).all()

    def get_grades_by_course(self, course_id):
        quizzes = self.get_quizzes_by_course(course_id)
        assignments = self.get_assignments_by_course(course_id)
        return {
            "quizzes": [{"title": quiz.title, "grade": quiz.grade} for quiz in quizzes],
            "assignments": [
                {"title": assignment.title, "grade": assignment.grade}
                for assignment in assignments
            ],
        }
