from django.urls import path
from student.views import registration, login,example

urlpatterns = [
    path("register/", registration, name = 'registration'),
    path("login/", login, name = 'login'),
    path("example/", example, name = 'example'),
]