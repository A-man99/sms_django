# Generated by Django 3.2.12 on 2023-02-04 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20230204_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff_registration',
            old_name='student_number',
            new_name='staff_number',
        ),
    ]