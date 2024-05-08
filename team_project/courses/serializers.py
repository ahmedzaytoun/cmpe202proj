from rest_framework import serializers
from .models import Course, Quiz, Assignment, Enrollment, Announcement
from faculty.serializers import FacultySerializer
from students.models import Student
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class StudentProfileSerializer(serializers.ModelSerializer):
    student_info = UserSerializer()

    class Meta:
        model = Student
        exclude = ["created_at", "updated_at"]

    def update(self, instance, validated_data):
        student_info_data = validated_data.pop("student_info", None)
        super().update(instance, validated_data)

        # Update nested User instance if data provided
        if student_info_data:
            user_serializer = UserSerializer(
                instance.student_info, data=student_info_data, partial=True
            )
            if user_serializer.is_valid():
                user_serializer.save()

        return instance


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz

        exclude = ["created_at", "updated_at"]


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment

        exclude = ["created_at", "updated_at"]


class CourseSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, required=False)
    assignments = AssignmentSerializer(many=True, required=False)
    course_name = serializers.SerializerMethodField()

    class Meta:
        model = Course

        exclude = ["created_at", "updated_at"]

    def get_course_name(self, obj):
        return obj.name


class EnrollmentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Enrollment
        fields = ["id", "courses"]


class AnnouncementSerializer(serializers.ModelSerializer):

    course_name = serializers.SerializerMethodField()
    faculty_name = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        exclude = ["created_at", "updated_at", "faculty", "courses"]

    def get_course_name(self, obj):
        return ", ".join(course.name for course in obj.courses.all())

    def get_faculty_name(self, obj):
        return obj.faculty.faculty_info.username
