from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('contact/', views.contact_page, name='contact'),
    path('about/', views.about_page, name='about'),
    path('faqs/', views.faqs_page, name='faqs'),
    path('policies/', views.policies_page, name='policies'),
    path('management/', views.management_page, name='management'),
    path('newsletter/', views.newsletter_signup, name='newsletter'),

]