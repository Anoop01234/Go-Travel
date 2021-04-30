from django.contrib import admin
from .models import DelhiRestaurant, ChennaiRestaurants, MumbaiRestaurants, KolkataRestaurants, PlacesMumbai, PlacesDelhi, PlacesChennai, PlacesKolkata
# Register your models here.

admin.site.register(DelhiRestaurant)
admin.site.register(ChennaiRestaurants)
admin.site.register(MumbaiRestaurants)
admin.site.register(KolkataRestaurants)
admin.site.register(PlacesDelhi)
admin.site.register(PlacesChennai)
admin.site.register(PlacesMumbai)
admin.site.register(PlacesKolkata)
