# Generated by Django 5.0.6 on 2024-05-08 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0012_alter_assignmentgrade_student_assignment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="faculty",
        ),
    ]
