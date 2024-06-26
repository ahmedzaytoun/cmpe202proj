# Generated by Django 5.0.6 on 2024-05-08 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_remove_enrollment_student_enrollment_student"),
        ("students", "0002_alter_student_notifications_enabled"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="student",
            field=models.ManyToManyField(
                related_name="enrollments", to="students.student"
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="Assignments",
            field=models.ManyToManyField(
                blank=True, related_name="courses", to="courses.assignment"
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="quizzes",
            field=models.ManyToManyField(
                blank=True, related_name="courses", to="courses.quiz"
            ),
        ),
        migrations.AlterField(
            model_name="grade",
            name="Quiz",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="grades_quiz",
                to="courses.quiz",
            ),
        ),
        migrations.AlterField(
            model_name="grade",
            name="assignment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="grades_assignment",
                to="courses.assignment",
            ),
        ),
        migrations.DeleteModel(
            name="Enrollment",
        ),
    ]
