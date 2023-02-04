from django.db import models
from cars.models import Cars
import datetime
from django.core.validators import MinValueValidator

NO = 0
YES = 1
CHOICES = {
    (NO, "No"),
    (YES, "Yes")
}

GP = 0
NATIONAL = 1
INDY = 2
LAYOUT = {
    (GP, "GP"),
    (NATIONAL, "National"),
    (INDY, "Indy"),
}

DECIBEL_LIMIT = ((0, '98db'), (1, '105db'))
HALF_OR_FULL_DAY = ((0, 'Half-day'), (1, 'Full-day'))


class Trackday(models.Model):

    """
    For storing information for upcoming track days
    """

    layout = models.IntegerField(choices=LAYOUT, default=GP)
    date = models.DateField(null=False, blank=False, default=None, validators=[MinValueValidator(datetime.date.today)])
    db_limit = models.BooleanField(choices=DECIBEL_LIMIT, default=0)
    car_hire = models.OneToOneField(Cars, on_delete=models.CASCADE, primary_key=True, null=False, blank=True)
    base_trackday_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.title)

    class Meta:
        """ Only one combo of Trackday and date permitted"""
        constraints = [
            models.UniqueConstraint(
                fields=['layout', 'date'],
                name='unique_trackday'),
        ]


class TrackdayBooking(models.Model):

    """
    For handling specific track day orders and their optional extras
    """
    trackday = models.ForeignKey(Trackday, on_delete=models.CASCADE)
    full_or_half_day = models.BooleanField(choices=HALF_OR_FULL_DAY, default=0)
    additional_drivers = models.BooleanField(choices=CHOICES, default=NO)
    helmet_hire = models.BooleanField(choices=CHOICES, default=NO)
    tuition = models.BooleanField(choices=CHOICES, default=NO)
    hospitality_packs = models.BooleanField(choices=CHOICES, default=NO)
    paddock_hire = models.BooleanField(choices=CHOICES, default=NO)

    def __str__(self):
        return str(self.title)



# Trackday Request Model Here:



# Experiences Model:



# Tuition Model:

