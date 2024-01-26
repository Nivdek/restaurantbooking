from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return self.username