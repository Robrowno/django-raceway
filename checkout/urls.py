from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('basket/', views.basket, name='basket'),
    path('checkout-success', views.checkout_success, name='success'),


]