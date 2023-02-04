from django.contrib.auth.models import User
from django.db import models

# Create your models here.

QUERY_TYPE = (
    (0, "General"),
    (1, "Trackdays/Experiences"),
    (2, "Bookings"),
    (3, "Other")
    )


class Contact(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=80)
    email = models.EmailField()
    query_type = models.CharField(max_length=11, choices=QUERY_TYPE, default=0)
    message = models.TextField()
    contacted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-contacted_on']

    def __str__(self):
        return f"{self.full_name} contacted you."
