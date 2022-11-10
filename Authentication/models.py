from email.headerregistry import Address
from enum import unique
from tabnanny import verbose
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from AddressComponent.models import Address

class User(AbstractUser):
    email = models.EmailField('email',unique=True)
    phoneNo = models.IntegerField('phone no', unique=True, null=True)
    position = models.CharField('position', max_length=150, null=True)
    address = models.ForeignKey(Address, verbose_name='address', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

    REQUIRED_FIELDS = []