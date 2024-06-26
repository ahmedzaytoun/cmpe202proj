# Generated by Django 5.0.6 on 2024-05-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0013_remove_course_faculty"),
        ("faculty", "0004_alter_faculty_created_at_alter_faculty_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="faculty",
            name="courses",
            field=models.ManyToManyField(
                blank=True, related_name="taught_courses", to="courses.course"
            ),
        ),
    ]
