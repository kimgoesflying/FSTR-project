from django.db import models
from django.utils.html import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from base64 import b64encode


class Tourist(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254, unique=True)
    phone = PhoneNumberField()

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'


class MountainPass(models.Model):

    beauty_title = models.CharField(max_length=64, null=True, blank=True)
    title = models.CharField(max_length=254, default='title')
    other_titles = models.CharField(max_length=254, null=True, blank=True)
    connect = models.CharField(max_length=64, null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        Tourist, on_delete=models.CASCADE, related_name='mountain_pass')

    status = models.CharField(
        max_length=8, default='new')

    latitude = models.DecimalField(
        max_digits=10, decimal_places=6, null=True)
    longitude = models.DecimalField(
        max_digits=10, decimal_places=6, null=True)
    height = models.IntegerField()

    level_winter = models.CharField(
        max_length=3, blank=True, default='')
    level_spring = models.CharField(
        max_length=3, blank=True, default='')
    level_summer = models.CharField(
        max_length=3, blank=True, default='')
    level_autumn = models.CharField(
        max_length=3, blank=True, default='')

    def __str__(self):
        return f'{self.title}'


class MountainPassImage(models.Model):
    mountainpass = models.ForeignKey(
        MountainPass, default=None, on_delete=models.CASCADE, related_name="images")
    date_add = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='images/', blank=True, null=True)
    binary_image = models.BinaryField(blank=True, null=True, editable=True)
    title = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f'{self.title}'

    def binary_image_tag(self):

        return mark_safe('<img src = "data: image/png; base64, {}" width="100" height="100">'.format(
            b64encode(self.binary_image).decode('utf8')
        ))

    binary_image_tag.short_description = 'Image'
    binary_image_tag.allow_tags = True
