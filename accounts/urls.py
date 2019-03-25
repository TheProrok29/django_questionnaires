from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('settings/', views.settings, name='settings'),
    path('change_password/', views.change_password, name='change_password'),
    path('change_data/', views.change_basic_data, name='change_data')
]
