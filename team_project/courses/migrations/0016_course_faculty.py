# Generated by Django 5.0.6 on 2024-05-08 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0015_remove_quizgrade_student_quiz_and_more"),
        ("faculty", "0006_remove_faculty_courses"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="faculty",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="courses_taught",
                to="faculty.faculty",
            ),
        ),
    ]