# Generated by Django 5.0.6 on 2024-05-08 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0004_remove_course_student"),
        ("students", "0002_alter_student_notifications_enabled"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="courses",
            field=models.ManyToManyField(
                related_name="enrollments", to="courses.course"
            ),
        ),
    ]
