from django.db import models

# Create your models here.
class DelhiRestaurant(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="Delhi/Restaurants/Images")
    location = models.TextField()
    hreftag = models.TextField()
