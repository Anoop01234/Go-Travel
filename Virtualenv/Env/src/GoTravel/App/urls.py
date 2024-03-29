from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('Delhi/Delhi.html',views.Delhi,name='Delhi'),
    path('Delhi/DelhiRestaurants.html',views.DelhiRestaurants,name='DelhiRestaurants'),
    path('Delhi/PlacesDelhi.html',views.PlaceDelhi,name='PlacesDelhi'),
    path('Delhi/EventsDelhi.html',views.EventDelhi,name='EventsDelhi'),
    path('Delhi/ShopsDelhi.html',views.ShopDelhi,name='ShopsDelhi'),
    path('Mumbai/Mumbai.html',views.Mumbai,name='Mumbai'),
    path('Mumbai/MumbaiRestaurants.html',views.MumbaiRestaurant,name='MumbaiRestaurants'),
    path('Mumbai/PlacesMumbai.html',views.PlaceMumbai,name='PlacesMumbai'),
    path('Mumbai/EventsMumbai.html',views.EventMumbai,name='EventsMumbai'),
    path('Mumbai/ShopsMumbai.html',views.ShopMumbai,name='ShopsMumbai'),
    path('Chennai/Chennai.html',views.Chennai,name='Chennai'),
    path('Chennai/ChennaiRestaurants.html',views.ChennaiRestaurant,name='ChennaiRestaurants'),
    path('Chennai/PlacesChennai.html',views.PlaceChennai,name='PlacesChennai'),
    path('Chennai/EventsChennai.html',views.EventChennai,name='EventsChennai'),
    path('Chennai/ShopsChennai.html',views.ShopChennai,name='ShopsChennai'),
    path('Kolkata/Kolkata.html',views.Kolkata,name='Kolkata'),
    path('Kolkata/KolkataRestaurants.html',views.KolkataRestaurant,name='KolkataRestaurants'),
    path('Kolkata/PlacesKolkata.html',views.PlaceKolkata,name='PlacesKolkata'),
    path('Kolkata/EventsKolkata.html',views.EventKolkata,name='EventsKolkata'),
    path('Kolkata/ShopsKolkata.html',views.ShopKolkata,name='ShopsKolkata'),
    path("Delhi/faq.html", views.faq , name="FAQ"),
    path("Mumbai/faq.html", views.faq , name="FAQ"),
    path("Chennai/faq.html", views.faq , name="FAQ"),
    path("Kolkata/faq.html", views.faq , name="FAQ"),
    path("Delhi/register.html",views.register, name="register")
]
