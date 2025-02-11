from django.db import models
from django.contrib.auth.models import User

class Student_details(models.Model):
    s_name=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    course=models.CharField(max_length=100)
    dob=models.DateField()

