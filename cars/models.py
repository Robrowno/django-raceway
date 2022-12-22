from django.db import models

# Create your models here.


class Cars(models.Model):

    FF = 0
    FR = 1
    MR = 2
    AWD = 3
    RR = 4
    DRIVETRAINS = [
        (FF, 'FrontEngine-FrontWheelDrive'),
        (FR, 'FrontEngine-RearWheelDrive'),
        (MR, 'MidEngine-RearWheelDrive'),
        (AWD, 'AllWheelDrive'),
        (RR, 'RearEngine-RearWheelDrive'),
    ]
    make = models.CharField(max_length=40, null=True, blank=True)
    model = models.CharField(max_length=40, null=True, blank=True)
    variant = models.CharField(max_length=40, null=False, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    power = models.PositiveIntegerField()
    torque = models.PositiveIntegerField()
    transmission = models.CharField(max_length=80)
    drivetrain = models.IntegerField(choices=DRIVETRAINS, default=None)
    cost_to_hire = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(f'{self.make} {self.model} {self.variant}')

    class Meta:
        verbose_name_plural = "Cars"
