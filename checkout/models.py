from django.db import models
from trackdays.models import TrackdayBooking, Tuition, Experiences
from profiles.models import UserProfile


# Create your models here.


class OrderItem(models.Model):

    """
    Order Information Model. Also generates unique
    order reference number.
    """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    trackday = models.ForeignKey(
        TrackdayBooking, on_delete=models.CASCADE, null=True, blank=True
        )
    tuition = models.ForeignKey(
        Tuition, on_delete=models.CASCADE, null=True, blank=True
        )
    experience = models.ForeignKey(
        Experiences, on_delete=models.CASCADE, null=True, blank=True
        )
    date = models.DateTimeField(auto_now_add=True)

    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)

    def _generate_order_number(self):
        """
        Generates a random and unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
