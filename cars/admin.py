from django.contrib import admin
from .models import Cars


@admin.register(Cars)
class CarAdmin(admin.ModelAdmin):

    """
    Admin Page for the Cars model.
    """
    list_display = ('make', 'model', 'variant',)
