# Generated by Django 5.0.6 on 2024-05-08 09:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("courses", "0005_remove_course_assignments_remove_course_quizzes_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Faculty",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "faculty_id",
                    models.PositiveBigIntegerField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                ("department", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "courses",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="faculty_courses",
                        to="courses.course",
                    ),
                ),
                (
                    "faculty_info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="faculty_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]