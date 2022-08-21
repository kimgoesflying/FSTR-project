from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Tourist(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField()

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'


class Coordinates(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=4)
    longitude = models.DecimalField(max_digits=10, decimal_places=4)
    height = models.IntegerField()


class MountainPass(models.Model):
    STATUS_TYPE = (
        ('n', 'new'),
        ('p', 'pending'),
        ('a', 'accepted'),
        ('r', 'rejected'),
    )

    LEVEL_TYPE = (
        ('0', ''),
        ('1', '1А'),
        ('2', '1Б'),
        ('3', '1Б*'),
        ('4', '2А'),
        ('5', '2Б*'),
        ('6', '2Б'),
        ('7', '3А'),
        ('8', '3Б'),
        ('9', '3Б*'),
    )

    beauty_title: models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=254, default='title')
    other_titles = models.CharField(max_length=254, null=True)
    connect = models.CharField(max_length=64, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_TYPE, default='')

    lvl_winter = models.CharField(
        max_length=1, choices=LEVEL_TYPE, default='0')
    lvl_spring = models.CharField(
        max_length=1, choices=LEVEL_TYPE, default='0')
    lvl_summer = models.CharField(
        max_length=1, choices=LEVEL_TYPE, default='0')
    lvl_autumn = models.CharField(
        max_length=1, choices=LEVEL_TYPE, default='0')

    def __str__(self):
        return f'{self.title}'

    def get_level(self):
        return {'winter': self.get_lvl_winter_display(),
                'spring': self.get_lvl_spring_display(),
                'summer': self.get_lvl_summer_display(),
                'autumn': self.get_lvl_autumn_display(),
                }

    def get_status(self):
        return self.get_status_display()


class MountainPassImage(models.Model):
    mountainpass = models.ForeignKey(
        MountainPass, default=None, on_delete=models.CASCADE, related_name="images")
    date_add = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    title = models.CharField(max_length=128, null=True)
