from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Delhi/Delhi.html',views.Delhi,name='Delhi'),
    path('Delhi/DelhiRestaurants.html',views.DelhiRestaurants,name='DelhiRestaurants'),
    path('Delhi/PlacesDelhi.html',views.PlaceDelhi,name='PlacesDelhi'),
    path('Delhi/EventsDelhi.html',views.EventsDelhi,name='EventsDelhi'),
    path('Delhi/ShopsDelhi.html',views.ShopsDelhi,name='ShopsDelhi'),
    path('Mumbai/Mumbai.html',views.Mumbai,name='Mumbai'),
    path('Mumbai/MumbaiRestaurants.html',views.MumbaiRestaurant,name='MumbaiRestaurants'),
    path('Mumbai/PlacesMumbai.html',views.PlaceMumbai,name='PlacesMumbai'),
    path('Mumbai/EventsMumbai.html',views.EventsMumbai,name='EventsMumbai'),
    path('Mumbai/ShopsMumbai.html',views.ShopsMumbai,name='ShopsMumbai'),
    path('Chennai/Chennai.html',views.Chennai,name='Chennai'),
    path('Chennai/ChennaiRestaurants.html',views.ChennaiRestaurant,name='ChennaiRestaurants'),
    path('Chennai/PlacesChennai.html',views.PlaceChennai,name='PlacesChennai'),
    path('Chennai/EventsChennai.html',views.EventsChennai,name='EventsChennai'),
    path('Chennai/ShopsChennai.html',views.ShopsChennai,name='ShopsChennai'),
    path('Kolkata/Kolkata.html',views.Kolkata,name='Kolkata'),
    path('Kolkata/KolkataRestaurants.html',views.KolkataRestaurant,name='KolkataRestaurants'),
    path('Kolkata/PlacesKolkata.html',views.PlaceKolkata,name='PlacesKolkata'),
    path('Kolkata/EventsKolkata.html',views.EventsKolkata,name='EventsKolkata'),
    path('Kolkata/ShopsKolkata.html',views.ShopsKolkata,name='ShopsKolkata'),

]
