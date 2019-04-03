from django.urls import path
from . import views

urlpatterns = [
    path('', views.surveys, name='surveys'),
    path('create/', views.create, name='create_survey'),
    path('<int:survey_id>/', views.survey, name='survey'),
    path('<int:survey_id>/delete/', views.delete, name='delete_survey'),
    path('<int:survey_id>/create_question', views.create_question, name='create_question'),
    path('<int:survey_id>/delete_question/<int:question_id>/', views.delete_question, name='delete_question'),
]
