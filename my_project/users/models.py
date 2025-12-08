from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

"""Models for selecting genders """
class Genders(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
"""Model to connect country with user to choose"""
class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

"""Custom User model """
class CustomUser(AbstractUser):
    gender = models.ForeignKey(
        Genders,
        on_delete=models.PROTECT,
        null=True,
        related_name='users',
        default=None)

    age = models.IntegerField(
        default=18,
        validators=[MinValueValidator(18), MaxValueValidator(150)],
    )

    country_born = models.ForeignKey(
        Country, on_delete=models.PROTECT,
        null=True,
        related_name='users',
        default=None)

    def __str__(self):
        return self.username
