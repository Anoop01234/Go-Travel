from django.contrib import admin
from .models import DelhiRestaurant, ChennaiRestaurants, MumbaiRestaurants, KolkataRestaurants, PlacesMumbai, PlacesDelhi, PlacesChennai, PlacesKolkata, EventsDelhi, EventsChennai, EventsKolkata, EventsMumbai, ShopsDelhi, ShopsChennai, ShopsKolkata, ShopsMumbai
# Register your models here.

admin.site.register(DelhiRestaurant)
admin.site.register(ChennaiRestaurants)
admin.site.register(MumbaiRestaurants)
admin.site.register(KolkataRestaurants)
admin.site.register(PlacesDelhi)
admin.site.register(PlacesChennai)
admin.site.register(PlacesMumbai)
admin.site.register(PlacesKolkata)
admin.site.register(EventsDelhi)
admin.site.register(EventsChennai)
admin.site.register(EventsKolkata)
admin.site.register(EventsMumbai)
admin.site.register(ShopsDelhi)
admin.site.register(ShopsChennai)
admin.site.register(ShopsKolkata)
admin.site.register(ShopsMumbai)
