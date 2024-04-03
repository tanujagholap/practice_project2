from django.core import validators
from django.db import models


class Create(models.Model):
    choice = [('male', 'MALE'), ('female', 'FEMALE')]
    cat_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=choice)
    color = models.CharField(max_length=20)
    weight = models.IntegerField()
    breed = models.CharField(max_length=20)

