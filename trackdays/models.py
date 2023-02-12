from django.db import models
from django.contrib.auth.models import User
from cars.models import Cars
import datetime
from django.core.validators import MinValueValidator, RegexValidator


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

BRONZE = 0
SILVER = 1
GOLD = 2
LEVELS = {
    (BRONZE, "Bronze"),
    (SILVER, "Silver"),
    (GOLD, "Gold"),
}

DECIBEL_LIMIT = ((0, '98db'), (1, '105db'))
HALF_OR_FULL_DAY = ((0, 'Half-day'), (1, 'Full-day'))


class Trackday(models.Model):

    """
    For storing information for upcoming track days
    """

    layout = models.IntegerField(choices=LAYOUT, default=GP)
    layout_image = models.ImageField(blank=True, null=True)
    date = models.DateField(null=False, blank=False, default=None, validators=[MinValueValidator(datetime.date.today)])
    db_limit = models.BooleanField(choices=DECIBEL_LIMIT, default=0)
    availability = models.IntegerField(default=30)
    base_trackday_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(f'{self.layout} trackday on {self.date}')

        """ Only one combo of Trackday and date permitted """
        constraints = [
            models.UniqueConstraint(
                fields=['layout', 'date'],
                name='unique_trackday'),
        ]


class TrackdayBooking(models.Model):

    """
    For handling specific track day orders and their optional extras
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    trackday = models.ForeignKey(Trackday, on_delete=models.CASCADE)
    car_hire = models.OneToOneField(Cars, on_delete=models.CASCADE, primary_key=True, blank=True)
    full_or_half_day = models.IntegerField(choices=HALF_OR_FULL_DAY, default=0)
    additional_drivers = models.PositiveIntegerField(default=0)
    helmet_hire = models.PositiveIntegerField(default=0)
    tuition = models.PositiveIntegerField(default=0)
    paddock_hire = models.IntegerField(choices=CHOICES, default=NO)

    def __str__(self):
        return str(f'{self.trackday} booking has been made')



class TrackdayRequest(models.Model):

    """
    Model for taking trackday requests
    """

    organiser = models.CharField(max_length=40)
    email = models.EmailField(null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message=(
            "Phone number must be entered in the format: '+999999999'."
            + "Up to 15 digits allowed."
            )
        )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
        )
    date_request = models.DateField(null=True, blank=True)
    full_or_half_day = models.IntegerField(choices=HALF_OR_FULL_DAY, default=0)
    number_of_spaces = models.IntegerField(null=True, blank=True)
    hospitality = models.IntegerField(choices=CHOICES, default=NO)
    pitlanes = models.IntegerField(choices=CHOICES, default=NO)
    db_limit = models.IntegerField(choices=DECIBEL_LIMIT, default=0)
    car_hire_required = models.IntegerField(choices=CHOICES, default=NO)


class Experiences(models.Model):

    """
    Model for the Experience Packages
    """

    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    itinerary = models.TextField(max_length=1000)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name_plural = "Experiences"

    def __str__(self):
        return str(self.title)


class Tuition(models.Model):

    """
    Model for the Tuition Packages
    """

    title = models.CharField(max_length=50)
    level = models.IntegerField(choices=LEVELS, default=None)
    description = models.TextField(max_length=1500)
    itinerary = models.TextField(max_length=1500)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    small_image = models.ImageField(null=True, blank=True)
    large_image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name_plural = "Tuition"

    def __str__(self):
        return str(self.title)
