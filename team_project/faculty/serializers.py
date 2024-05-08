from rest_framework import serializers
from .models import Faculty


class FacultySerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = ["username"]

    def get_username(self, obj):
        return obj.faculty_info.username if obj.faculty_info else None
