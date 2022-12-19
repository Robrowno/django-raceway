from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    """
    Admin Page for the Contact model.
    """
    list_display = ('full_name', 'email', 'query_type', 'contacted_on')
    readonly_fields = ('contacted_on',)
