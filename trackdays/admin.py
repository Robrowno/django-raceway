from django.contrib import admin
from .models import (
    Trackday, TrackdayBooking, Experiences, Tuition, TrackdayRequest
    )
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Trackday)
class TrackdayAdmin(admin.ModelAdmin):

    """
    Admin Page for the Trackday model.
    """
    list_display = ('date', 'layout',)


@admin.register(TrackdayBooking)
class TrackdayBookingAdmin(admin.ModelAdmin):

    """
    Admin Page for the Trackday Bookings model.
    """
    list_display = ('trackday', 'full_or_half_day',)
    readonly_fields = ('trackday',)


@admin.register(TrackdayRequest)
class RequestAdmin(admin.ModelAdmin):

    """
    Admin Page for the TrackdayRequest model.
    """
    list_display = ('organiser', 'email', 'date_request', 'number_of_spaces')


@admin.register(Experiences)
class ExperiencesAdmin(SummernoteModelAdmin):

    """
    Admin Page for the Experiences model
    """
    list_display = ('title', )
    summernote_fields = ('itinerary',)


@admin.register(Tuition)
class TuitionAdmin(SummernoteModelAdmin):

    """
    Admin Page for the Tuition model
    """

    list_display = ('title', 'level')
    summernote_fields = ('itinerary', 'description')
