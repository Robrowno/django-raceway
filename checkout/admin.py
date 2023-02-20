from django.contrib import admin
from checkout.models import OrderItem


@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin Page for the OrderItem model.
    """
    list_display = ('user_profile', 'date')
