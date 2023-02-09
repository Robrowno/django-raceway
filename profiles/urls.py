from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='updateProfile'),
]
