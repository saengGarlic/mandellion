
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Pot(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    potName = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    regDate = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200, default='')

    potTypeList = (
        ('Tower', 'Vertical Tower'), ('Reservoir', 'Flat Bed Reservoir'),
        ('Pipe', 'Single Line Pipe'),
    )

    potType = models.CharField(max_length=20, choices=potTypeList, default='Tower')

    def __str__(self):
        return (self.potName + ' of ' + self.owner)


class PlantInfo(models.Model):
    Pot = models.ForeignKey(Pot, on_delete=models.CASCADE)
    plantName = models.CharField(max_length=50)
    plantedDate = models.DateTimeField(auto_now_add=True)
