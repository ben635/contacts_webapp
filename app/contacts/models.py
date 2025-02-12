from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=240)
    telephone_number = PhoneNumberField(region="GB")

    def __str__(self):
        return self.name