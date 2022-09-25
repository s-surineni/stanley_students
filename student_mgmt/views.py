from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from student_mgmt.forms import StudentForm
from student_mgmt.models import Student


def student(request):
    student_form = StudentForm(request.POST or None, request.FILES or None)
    context = {'form': student_form, 'page_title': 'Add Student'}
    if request.method == 'POST':
        if student_form.is_valid():
            user_name = student_form.cleaned_data.get('user_name')
            first_name = student_form.cleaned_data.get('first_name')
            last_name = student_form.cleaned_data.get('last_name')
            course = student_form.cleaned_data.get('course')
            try:
                user = Student(
                    user_name=user_name, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, "Successfully Added")
                return redirect(reverse('add_student'))
            except Exception as e:
                messages.error(request, "Could Not Add: " + str(e))
        else:
            messages.error(request, "Could Not Add: ")
    return render(request, 'add_student.html', context)