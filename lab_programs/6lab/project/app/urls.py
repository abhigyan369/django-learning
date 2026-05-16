from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.project_view),
    path('show/', views.show_projects),
]