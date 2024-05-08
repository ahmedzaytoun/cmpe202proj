from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Enrollment, Course
from .serializers import CourseSerializer

from students.models import Student
from courses.models import QuizGrade, AssignmentGrade
from .serializers import (
    EnrollmentSerializer,
    QuizGradeSerializer,
    AssignmentGradeSerializer,
)
from .serializers import StudentProfileSerializer


from .models import Enrollment
from .serializers import CourseSerializer
from courses.models import QuizGrade, StudentQuiz


class EnrolledCoursesView(APIView):
    def get(self, request, *args, **kwargs):
        # Fetch the Student instance based on the student_info link to User
        user = request.user
        student = get_object_or_404(
            Student, student_info=user
        )  # Use the correct field name here

        # Fetch all enrollments for the student
        enrollments = Enrollment.objects.filter(student=student)

        # Extract all courses from the enrollments where the course is published
        courses = [
            enrollment.course
            for enrollment in enrollments
            if enrollment.course.is_published
        ]

        # Serialize the courses
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class CourseContentView(APIView):
    def get(self, request, courseId, *args, **kwargs):
        course = Course.objects.filter(id=courseId, is_published=True).first()
        if not course:
            return Response(
                {"error": "Course not found or is not published"}, status=404
            )
        serializer = CourseSerializer(course)
        return Response(serializer.data)


class CourseGradesView(APIView):
    def get(self, request, courseId, *args, **kwargs):
        user = request.user
        student = get_object_or_404(
            Student, student_info=user
        )  # Adjust this based on your user-student relationship

        # Get student quizzes linked to the specified course
        student_quizzes = StudentQuiz.objects.filter(
            student=student, quiz__course_id=courseId
        )

        # Now fetch grades for these quizzes
        quiz_grades = QuizGrade.objects.filter(student_quiz__in=student_quizzes)

        # Assuming you have a serializer for QuizGrade
        serializer = QuizGradeSerializer(quiz_grades, many=True)
        return Response(serializer.data)


class UpdateProfileView(APIView):
    def put(self, request, *args, **kwargs):
        student = request.user.student_profile
        serializer = StudentProfileSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
