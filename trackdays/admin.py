from django.contrib import admin
from .models import Trackday, TrackdayBooking, Experiences, Tuition, TrackdayRequest

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


@admin.register(TrackdayRequest)
class RequestAdmin(admin.ModelAdmin):

    """
    Admin Page for the TrackdayRequest model.
    """
    list_display = ('organiser', 'email', 'date_request', 'number_of_spaces')


@admin.register(Experiences)
class ExperiencesAdmin(admin.ModelAdmin):

    """
    Admin Page for the Experiences model
    """
    list_display = ('title', )


@admin.register(Tuition)
class TuitionAdmin(admin.ModelAdmin):

    """
    Admin Page for the Tuition model
    """

    list_display = ('title', 'level')