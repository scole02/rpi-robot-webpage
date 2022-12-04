from django.db import models

# Create your models here.

class GPS(models.Model):
    datetime = models.DateTimeField()
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)
