# Generated by Django 5.0.6 on 2024-05-08 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("faculty", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="faculty",
            options={"verbose_name_plural": "Faculties"},
        ),
        migrations.RemoveField(
            model_name="faculty",
            name="courses",
        ),
    ]
