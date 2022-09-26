from django import forms
from .models import Course, Student


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name']


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['user_name', 'first_name', 'last_name', 'course']
