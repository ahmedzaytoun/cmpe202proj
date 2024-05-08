from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Faculty
from courses.serializers import (
    CourseSerializer,
    AssignmentSerializer,
    QuizSerializer,
    AnnouncementSerializer,
)
from courses.models import (
    Course,
    FacultyTeaching,
    Enrollment,
    Quiz,
    Assignment,
    Announcement,
)
from django.shortcuts import get_object_or_404
from rest_framework import status
from students.serializers import StudentSerializer


class FacultyCoursesView(APIView):
    def get(self, request):

        user = request.user
        faculty = get_object_or_404(Faculty, faculty_info=user)  #

        courses = Course.objects.filter(faculty=faculty)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class AddCourseContentView(APIView):
    def get(self, request, courseId):
        user = request.user
        faculty = get_object_or_404(
            Faculty, faculty_info=user
        )  # Ensure Faculty model has a user field as OneToOneField

        # Fetch all teaching assignments for this faculty that are active
        teaching_assignments = FacultyTeaching.objects.filter(
            faculty=faculty, course__id=courseId
        )

        # Extract the courses from the teaching assignments
        courses = [assignment.course for assignment in teaching_assignments]

        # Serialize the active courses
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, courseId):
        user = request.user
        faculty = get_object_or_404(Faculty, faculty_info=user)  #
        course = get_object_or_404(Course, id=courseId, faculty=faculty)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseStudentsView(APIView):
    def get(self, request, courseId):
        user = request.user
        faculty = get_object_or_404(Faculty, faculty_info=user)
        course = get_object_or_404(Course, id=courseId, faculty=faculty)  #
        enrollments = Enrollment.objects.filter(course=course)
        students = [
            enrollment.student for enrollment in enrollments
        ]  # Extracting students from enrollments
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class AddAssignmentView(APIView):

    def get(self, request, courseId):
        user = request.user
        faculty = get_object_or_404(Faculty, faculty_info=user)
        course = get_object_or_404(Course, id=courseId, faculty=faculty)
        print(course)
        assignments = course.assignments.all()
        print(assignments)
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    def post(self, request, courseId):
        user = request.user
        faculty = get_object_or_404(Faculty, faculty_info=user)
        course = get_object_or_404(Course, id=courseId, faculty=faculty)  #
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(course=course)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseGradesView(APIView):

    def get(self, request, courseId):
        user = request.user
        faculty = get_object_or_404(Faculty, faculty_info=user)
        course = get_object_or_404(Course, id=courseId, faculty=faculty)  #
        quizzes = Quiz.objects.filter(course=course)
        assignments = Assignment.objects.filter(course=course)
        quiz_serializer = QuizSerializer(quizzes, many=True)
        assignment_serializer = AssignmentSerializer(assignments, many=True)
        return Response(
            {"quizzes": quiz_serializer.data, "assignments": assignment_serializer.data}
        )

    def put(self, request, courseId):
        # Updating a specific quiz or assignment requires identifying it by ID
        # This is a simple implementation, you might want to restrict updates to specific fields like 'grade'
        quiz_data = request.data.get("quizzes")
        assignment_data = request.data.get("assignments")

        if quiz_data:
            for quiz in quiz_data:
                quiz_instance = Quiz.objects.get(id=quiz["id"], course_id=courseId)
                quiz_serializer = QuizSerializer(quiz_instance, data=quiz, partial=True)
                if quiz_serializer.is_valid():
                    quiz_serializer.save()

        if assignment_data:
            for assignment in assignment_data:
                assignment_instance = Assignment.objects.get(
                    id=assignment["id"], course_id=courseId
                )
                assignment_serializer = AssignmentSerializer(
                    assignment_instance, data=assignment, partial=True
                )
                if assignment_serializer.is_valid():
                    assignment_serializer.save()

        return Response(
            {"message": "Grades updated successfully"}, status=status.HTTP_200_OK
        )


class AnnouncementView(APIView):
    def get(self, request, courseId):
        # Retrieve the faculty member based on the logged-in user
        user = request.user
        faculty = get_object_or_404(Faculty, faculty_info=user)
        course = get_object_or_404(Course, id=courseId, faculty=faculty)

        announcements = Announcement.objects.filter(courses=course)

        # Serialize the fetched announcements
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)

    def post(self, request, courseId):
        # Handle posting a new announcement
        user = request.user
        faculty = get_object_or_404(Faculty, faculty_info=user)
        course = get_object_or_404(Course, id=courseId, faculty=faculty)
        if not course.faculty == faculty:
            return Response(
                {"error": "Faculty not associated with this course"},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = AnnouncementSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            announcement = serializer.save(faculty=faculty)
            announcement.courses.add(
                course
            )  # Link the announcement to the specific course
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
