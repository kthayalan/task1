from django.db import models

# Create your models here.
from tabnanny import verbose
from django.db import models

# Create your models here.

from django.db import models


class State(models.Model):
    code = models.IntegerField('state code')
    name = models.CharField('state name', max_length=150)
    country = models.CharField('country', max_length=150)


class Locality(models.Model):
    code = models.IntegerField('locality code')
    name = models.CharField('locality name', max_length=150)
    state = models.ForeignKey(State, verbose_name="state", on_delete=models.CASCADE, null=True)


class Postcode(models.Model):
    code = models.IntegerField('post code')
    state = models.ForeignKey(State, verbose_name='state', on_delete=models.CASCADE, null=True)


class LocalPostalCode(models.Model):
    name = models.CharField('local postal code name', max_length=150)
    locality = models.ForeignKey(Locality, verbose_name='locality', on_delete=models.CASCADE, null=True)
    postcode = models.IntegerField('postal code')


class Street(models.Model):
    name = models.CharField('street name', max_length=150)
    local_postal_code = models.ForeignKey(LocalPostalCode, verbose_name='local postal code', on_delete=models.CASCADE,
                                          null=True)


class Address(models.Model):
    no = models.IntegerField('no')
    address_1 = models.CharField('address_1', max_length=150)
    street = models.ForeignKey(Street, verbose_name='street', on_delete=models.CASCADE, null=True)
