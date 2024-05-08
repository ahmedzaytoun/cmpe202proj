from django.db import models
from common.models import CommonModel

# Create your models here.


class Faculty(CommonModel):
    faculty_info = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="faculty_profile"
    )
    faculty_id = models.PositiveBigIntegerField(unique=True, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.faculty_info} - {self.department}"

    def taught_courses(self):
        return self.faculty_teaching.all()

    class Meta:
        verbose_name_plural = "Faculties"
