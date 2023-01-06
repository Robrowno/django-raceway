from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('basket/', views.basket, name='basket'),
    path('basket/add/<experience_id>/', views.add_exp_to_basket, name='add_exp_to_basket'),
    path('basket/add/<tuition_id>/', views.add_tuition_to_basket, name='add_tuition_to_basket'),
    path('checkout-success/', views.checkout_success, name='success'),

]
