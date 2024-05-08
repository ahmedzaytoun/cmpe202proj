from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ["username"]

    def get_username(self, obj):
        # Assuming 'student_info' is the related name to the User model
        return obj.student_info.username if obj.student_info else None


class StudentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        exclude = ["created_at", "updated_at"]

    enrolled_courses = serializers.StringRelatedField(many=True)

    def get_enrolled_courses(self, obj):

        return obj.enrolled_courses.all()
