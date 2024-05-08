from django.db import models
from common.models import CommonModel


# Create your models here.
class SchoolAdmin(CommonModel):
    user = models.OneToOneField(
        "users.user", on_delete=models.CASCADE, related_name="admin_profile"
    )

    def __str__(self):
        return self.user.username
