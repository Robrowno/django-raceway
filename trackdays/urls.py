from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.track_day_list,
        name='trackdays'),
    path(
        'trackday-booking/<trackday_id>/',
        views.track_day_detail,
        name='booking'),
    path(
        'trackday-request/',
        views.track_day_request,
        name='request'),
    path(
        'experiences/',
        views.experiences,
        name='experiences'),
    path(
        'experiences/<experience_id>/',
        views.experiences_detail,
        name='exp_detail'),
    path(
        'tuition/',
        views.tuition,
        name='tuition'),
    path(
        'tuition/<tuition_id>/',
        views.tuition_detail,
        name='tuition_detail'),
]
