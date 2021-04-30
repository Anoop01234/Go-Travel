from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import DelhiRestaurant, ChennaiRestaurants, MumbaiRestaurants, KolkataRestaurants, PlacesMumbai, PlacesDelhi, PlacesChennai, PlacesKolkata
# Create your views here
def index(request):
    return  render(request,'HomePage/index.html')
def Delhi(request):
    return render(request,'Delhi/Delhi.html')
def DelhiRestaurants(request):
    rests=DelhiRestaurant.objects.all()
    return render(request,'Delhi/DelhiRestaurants.html',{'rests': rests})
def PlaceDelhi(request):
    rests=PlacesDelhi.objects.all()
    return render(request,'Mumbai/PlacesDelhi.html',{'rests': rests})
def EventsDelhi(request):
    return render(request,'Delhi/EventsDelhi.html')
def ShopsDelhi(request):
    return render(request,'Delhi/ShopsDelhi.html')
def Mumbai(request):
    return render(request,'Mumbai/Mumbai.html')
def MumbaiRestaurant(request):
    rests=MumbaiRestaurants.objects.all()
    return render(request,'Mumbai/MumbaiRestaurants.html',{'rests': rests})
def PlaceMumbai(request):
    rests=PlacesMumbai.objects.all()
    return render(request,'Mumbai/PlacesMumbai.html',{'rests': rests})
def EventsMumbai(request):
    return render(request,'Mumbai/EventsMumbai.html')
def ShopsMumbai(request):
    return render(request,'Mumbai/ShopsMumbai.html')
def Chennai(request):
    return render(request,'Chennai/Chennai.html')
def ChennaiRestaurant(request):
    rests=ChennaiRestaurants.objects.all()
    return render(request,'Chennai/ChennaiRestaurants.html',{'rests': rests})
def PlaceChennai(request):
    rests=PlacesChennai.objects.all()
    return render(request,'Chennai/PlacesChennai.html',{'rests': rests})
def EventsChennai(request):
    return render(request,'Chennai/EventsChennai.html')
def ShopsChennai(request):
    return render(request,'Chennai/ShopsChennai.html')
def Kolkata(request):
    return render(request,'Kolkata/Kolkata.html')
def KolkataRestaurant(request):
    rests=KolkataRestaurants.objects.all()
    return render(request,'Kolkata/KolkataRestaurants.html',{'rests': rests})
def PlaceKolkata(request):
    rests=PlacesKolkata.objects.all()
    return render(request,'Kolkata/PlacesKolkata.html',{'rests': rests})
def EventsKolkata(request):
    return render(request,'Kolkata/EventsKolkata.html')
def ShopsKolkata(request):
    return render(request,'Kolkata/ShopsKolkata.html')

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message   = request.POST['message']
        return render(request,"index.html",{'message_name':message_name})
    else:
        return render(request,"index.html",{})