from django.db import models
from trackdays.models import TrackdayBooking, Tuition, Experiences
from profiles.models import UserProfile


# Create your models here.


class OrderItem(models.Model):

    """
    Order Information Model. .
    """

    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    date = models.DateTimeField(auto_now_add=True)
    stripe_reciept=models.TextField(default=None)

    def __str__(self):
        return self.stripe_reciept