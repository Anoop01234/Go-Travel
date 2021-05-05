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
class PlacesMumbai(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Mumbai/Places")
    location = models.TextField()
    hreftag = models.TextField()
class PlacesDelhi(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Delhi/Places")
    location = models.TextField()
    hreftag = models.TextField()
class PlacesChennai(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Chennai/Places")
    location = models.TextField()
    hreftag = models.TextField()
class PlacesKolkata(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Kolkata/Places")
    location = models.TextField()
    hreftag = models.TextField()
class EventsDelhi(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Delhi/Events")
    location = models.TextField()
    hreftag = models.TextField()
class EventsChennai(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Chennai/Events")
    location = models.TextField()
    hreftag = models.TextField()
class EventsKolkata(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Kolkata/Events")
    location = models.TextField()
    hreftag = models.TextField()
class EventsMumbai(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Mumbai/Events")
    location = models.TextField()
    hreftag = models.TextField()
class ShopsDelhi(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Delhi/Events")
    location = models.TextField()
    hreftag = models.TextField()
class ShopsChennai(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Chennai/Events")
    location = models.TextField()
    hreftag = models.TextField()
class ShopsKolkata(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Kolkata/Events")
    location = models.TextField()
    hreftag = models.TextField()
class ShopsMumbai(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Images/Mumbai/Events")
    location = models.TextField()
    hreftag = models.TextField()