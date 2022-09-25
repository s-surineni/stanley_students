from django.contrib.auth.models import AbstractUser
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    GENDER = [("M", "Male"), ("F", "Female")]

    user_name = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True, blank=False)

    def __str__(self):
        return self.last_name + ", " + self.first_name