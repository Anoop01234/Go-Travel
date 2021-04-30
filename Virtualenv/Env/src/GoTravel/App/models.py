from django.db import models

# Create your models here.
class DelhiRestaurant(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Delhi/Restaurants")
    location = models.TextField()
    hreftag = models.TextField()
class ChennaiRestaurants(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Chennai/Restaurants")
    location = models.TextField()
    hreftag = models.TextField()
class MumbaiRestaurants(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Mumbai/Restaurants")
    location = models.TextField()
    hreftag = models.TextField()
class KolkataRestaurants(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Kolkata/Restaurants")
    location = models.TextField()
    hreftag = models.TextField()