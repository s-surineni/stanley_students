from django.urls import path
from . import views

urlpatterns = [
    path("student/", views.student, name='student'),
    path("course/", views.course, name='course'),
]