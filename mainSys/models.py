
from django.db import models
from datetime import datetime

class Pot(models.Model):

    startDate = models.DateField(Default)
    location = models.CharField(max_length=20)

    def __str__(self):
        return (self.plantName + ' - ' + self.startDate)

class PlantInfo(models.Model):
    plantName = models.CharField(max_length=50)