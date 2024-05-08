# Generated by Django 5.0.6 on 2024-05-08 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
        ("students", "0002_alter_student_notifications_enabled"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="enrollment",
            name="student",
        ),
        migrations.AddField(
            model_name="enrollment",
            name="student",
            field=models.ManyToManyField(
                related_name="enrollments", to="students.student"
            ),
        ),
    ]