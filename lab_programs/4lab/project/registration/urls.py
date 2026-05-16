from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_student, name='register'),
    path('students/', views.course_students, name='course_students'),
]