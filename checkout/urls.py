from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('basket/', views.basket, name='my_basket'),
    path('basket/add/experience/<experience_id>/', views.add_exp_to_basket, name='add_exp_to_basket'),
    path('basket/add/tuition/<tuition_id>/', views.add_tuition_to_basket, name='add_tuition_to_basket'),
    path('basket/adjust/<item_id>/', views.edit_basket, name='adjust'),
    path('checkout-success/', views.checkout_success, name='success'),

]
