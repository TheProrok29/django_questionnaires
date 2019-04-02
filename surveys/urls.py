from django.urls import path
from . import views

urlpatterns = [
    path('', views.surveys, name='surveys'),
    path('create/', views.create, name='create_survey'),
]
