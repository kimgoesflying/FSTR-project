from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Tourist(models.Model):
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField()

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
