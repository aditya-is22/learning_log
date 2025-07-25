# users/urls.py

"""Defines URL patterns for users."""

from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # Include default auth urls for login and logout.
    path('', include('django.contrib.auth.urls')),
    
    # Registration page
    path('register/', views.register, name='register'),
]