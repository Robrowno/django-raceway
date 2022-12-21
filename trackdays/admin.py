from django.contrib import admin
from .models import Trackday, TrackdayBooking

# Register your models here.


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
