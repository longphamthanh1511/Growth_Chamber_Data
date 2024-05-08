from django.db import models

class Plants(models.Model):
    kigo=models.CharField(max_length=100)
    temp=models.FloatField(max_length=150)
    hum=models.FloatField(max_length=150)
    sun=models.FloatField(max_length=150)
    co2=models.FloatField(max_length=150)
    water=models.FloatField(max_length=150)
    time=models.CharField(max_length=150)