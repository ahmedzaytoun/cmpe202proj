from rest_framework.views import APIView
from . import serializers
from .models import Student
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    ParseError,
    PermissionDenied,
)
from django.shortcuts import get_object_or_404
from courses.models import Course, Enrollment
from courses.serializers import CourseSerializer, QuizSerializer, AssignmentSerializer

# Create your views here.


class StudentsView(APIView):

    def get(self, request):
        all_students = Student.objects.all()
        serializer = serializers.StudentSerializer(
            all_students, many=True, context={"request": request}
        )
        return Response(serializer.data)


class StudentDetailView(APIView):

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = serializers.StudentDetailSerializer(
            student, context={"request": request}
        )
        return Response(serializer.data)


class EnrolledCoursesView(APIView):
    def get(self, request):
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
    def get(self, request, courseId):
        course = Course.objects.filter(id=courseId, is_published=True).first()
        if not course:
            return Response(
                {"error": "Course not found or is not published"}, status=404
            )
        serializer = CourseSerializer(course)
        return Response(serializer.data)


class StudentCourseGradesView(APIView):
    def get(self, request, courseId):
        course = Course.objects.filter(id=courseId, is_published=True).first()
        if not course:
            return Response(
                {"error": "Course not found or is not published"}, status=404
            )
        user = request.user
        student = get_object_or_404(Student, student_info=user)

        quizzes = student.student_quizzes.filter(course=course)
        assignments = student.student_assignments.filter(course=course)

        # Serializing the data
        quiz_serializer = QuizSerializer(quizzes, many=True)
        assignment_serializer = AssignmentSerializer(assignments, many=True)

        # Compiling all grades into a single response
        grades_data = {
            "quizzes": quiz_serializer.data,
            "assignments": assignment_serializer.data,
        }

        return Response(grades_data)
