# Generated by Django 5.0.1 on 2024-01-18 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('photo', models.FileField(blank=True, null=True, upload_to='student_photos/')),
                ('resume', models.FileField(blank=True, null=True, upload_to='student_resumes/')),
            ],
        ),
    ]