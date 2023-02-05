# Generated by Django 3.2.12 on 2023-02-03 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('destination', models.CharField(blank=True, max_length=100, null=True)),
                ('event_date', models.CharField(max_length=100)),
                ('event_description', models.TextField()),
                ('date', models.DateField()),
                ('event_thumbnail', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='staff_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=100, null=True)),
                ('date_of_birth', models.CharField(max_length=1000, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('faculty_type', models.CharField(choices=[('Teaching', 'Teaching'), ('HOD', 'HOD'), ('Assistant Teacher', 'Assistant Teacher'), ('Assistant HOD', 'Assistant HOD'), ('NON-Teaching', 'NON-Teaching')], max_length=100)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='student_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.CharField(max_length=1000, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('course', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
