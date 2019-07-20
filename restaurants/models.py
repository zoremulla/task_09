from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    logo = models.ImageField(upload_to='restaurant_logos', null=True, blank=True)

    def __str__(self):
    	return self.name
class User(models.Model):
    Username= models.CharField(max_length=70)
    First_name=models.CharField(max_length=120)
    Last_name=models.CharField(max_length=120)
    Email=models.EmailField(max_length=60)
    Password=models.CharField(max_length=11)