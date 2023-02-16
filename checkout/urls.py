from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('basket/', views.basket, name='my_basket'),
    path('basket/add/trackday/<trackday_id>/', views.add_trackday_to_basket, name='add_td_to_basket'),
    path('basket/remove/trackday/<item_id>/', views.remove_trackday_from_basket, name='rmv_trackday'),
    path('basket/add/experience/<experience_id>/', views.add_exp_to_basket, name='add_exp_to_basket'),
    path('basket/add/tuition/<tuition_id>/', views.add_tuition_to_basket, name='add_tuition_to_basket'),
    path('basket/adjust/experience/<item_id>/', views.edit_exp_quantity, name='edit_exp'),
    path('basket/adjust/tuition/<item_id>/', views.edit_tuition_quantity, name='edit_tuition'),
    path('basket/remove/experience/<item_id>/', views.remove_exp, name='rmv_exp'),
    path('basket/remove/tuition/<item_id>/', views.remove_tuition, name='rmv_tuition'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('error/', views.error, name='error'),
    path('history/', views.history, name='history'),
]
