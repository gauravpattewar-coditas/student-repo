# myproject/student/models.py
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    photo = models.FileField(upload_to='student_photos/', null=True, blank=True)
    resume = models.FileField(upload_to='student_resumes/', null=True, blank=True)

