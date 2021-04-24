from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import DelhiRestaurant, ChennaiRestaurants
# Create your views here
def index(request):
    return  render(request,'HomePage/index.html')
def Delhi(request):
    return render(request,'Delhi/Delhi.html')
def DelhiRestaurants(request):
    rests=DelhiRestaurant.objects.all()
    return render(request,'Delhi/DelhiRestaurants.html',{'rests': rests})
def PlacesDelhi(request):
    return render(request,'Delhi/PlacesDelhi.html')
def EventsDelhi(request):
    return render(request,'Delhi/EventsDelhi.html')
def ShopsDelhi(request):
    return render(request,'Delhi/ShopsDelhi.html')
def Mumbai(request):
    return render(request,'Mumbai/Mumbai.html')
def MumbaiRestaurants(request):
    return render(request,'Mumbai/MumbaiRestaurants.html')
def PlacesMumbai(request):
    return render(request,'Mumbai/PlacesMumbai.html')
def EventsMumbai(request):
    return render(request,'Mumbai/EventsMumbai.html')
def ShopsMumbai(request):
    return render(request,'Mumbai/ShopsMumbai.html')
def Chennai(request):
    return render(request,'Chennai/Chennai.html')
def ChennaiRestaurants(request):
    return render(request,'Chennai/ChennaiRestaurants.html')
def PlacesChennai(request):
    return render(request,'Chennai/PlacesChennai.html')
def EventsChennai(request):
    return render(request,'Chennai/EventsChennai.html')
def ShopsChennai(request):
    return render(request,'Chennai/ShopsChennai.html')
def Kolkata(request):
    return render(request,'Kolkata/Kolkata.html')
def KolkataRestaurants(request):
    return render(request,'Kolkata/KolkataRestaurants.html')
def PlacesKolkata(request):
    return render(request,'Kolkata/PlacesKolkata.html')
def EventsKolkata(request):
    return render(request,'Kolkata/EventsKolkata.html')
def ShopsKolkata(request):
    return render(request,'Kolkata/ShopsKolkata.html')
