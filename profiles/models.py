from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField


# Create your models here.


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20,
                                            null=True, blank=True, default='')
    default_email_address = models.CharField(max_length=50,
                                             null=True, blank=True, default='')
    default_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True, default='')
    default_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True, default='')
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True, default='')
    default_county = models.CharField(max_length=80,
                                      null=True, blank=True, default='')
    default_postcode = models.CharField(max_length=20,
                                        null=True, blank=True, default='')
    default_nationality = CountryField(
        blank_label='Nationality', null=True, blank=True, default=''
        )

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        """
        Create or update the user profile
        """
        if created:
            UserProfile.objects.create(user=instance)
        instance.userprofile.save()


class CardStorage(models.Model):
    """
    Storing Default Credit Card for User
    """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name_on_card = models.CharField(max_length=50)
    cc_number = CardNumberField('card number')
    cc_expiry = CardExpiryField('expiration date')
    cc_code = SecurityCodeField('security code')

    def __str__(self):
        return str(f"{self.user}'s card has been stored")
