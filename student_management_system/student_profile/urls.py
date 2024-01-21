from django.contrib import admin
from django.urls import path
from .views import student,delete_student, student_list, edit_student
urlpatterns = [
    path('profile/', student, name='student'),
    path('delete/<int:pk>/', delete_student, name='delete_student'),
    path('/', student_list, name='student_list'),
    path('edit/<int:pk>/', edit_student, name='edit_student'),
]