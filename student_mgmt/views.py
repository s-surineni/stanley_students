import logging

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from student_mgmt.forms import CourseForm, StudentForm
from student_mgmt.models import Student, Course


def student(request):
    student_form = StudentForm(request.POST or None)
    context = {'form': student_form, 'page_title': 'Add Student'}
    if request.method == 'POST':
        if student_form.is_valid():
            user_name = student_form.cleaned_data.get('user_name')
            first_name = student_form.cleaned_data.get('first_name')
            last_name = student_form.cleaned_data.get('last_name')
            course = student_form.cleaned_data.get('course')
            try:
                user = Student(
                    user_name=user_name, first_name=first_name,
                    last_name=last_name, course=course)
                user.save()
                messages.success(request, "Successfully Added")
                return redirect(reverse('student'))
            except Exception as e:
                messages.error(request, "Could Not Add: " + str(e))
        else:
            messages.error(request, "Could Not Add: ")
    return render(request, 'add_student.html', context)


def course(request):
    course_form = CourseForm(request.POST or None)
    context = {'form': course_form, 'page_title': 'Add Course'}
    if request.method == 'POST':
        if course_form.is_valid():
            name = course_form.cleaned_data.get('name')
            try:
                course_ob = Course(
                    name=name)
                course_ob.save()
                messages.success(request, "Successfully Added")
                return redirect(reverse('course'))
            except Exception as e:
                messages.error(request, "Could Not Add: " + str(e))
                logging.exception("error saving course")
        else:
            messages.error(request, "Could Not Add: ")
    return render(request, 'add_course.html', context)