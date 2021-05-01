from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import DelhiRestaurant, ChennaiRestaurants, MumbaiRestaurants, KolkataRestaurants, PlacesMumbai, PlacesDelhi, PlacesChennai, PlacesKolkata, EventsDelhi, EventsChennai, EventsKolkata, EventsMumbai, ShopsDelhi, ShopsChennai, ShopsKolkata, ShopsMumbai
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
    return render(request,'Delhi/PlacesDelhi.html',{'rests': rests})
def EventDelhi(request):
    rests=EventsDelhi.objects.all()
    return render(request,'Delhi/EventsDelhi.html',{'rests': rests})
def ShopDelhi(request):
    rests=ShopsDelhi.objects.all()
    return render(request,'Delhi/ShopsDelhi.html',{'rests': rests})
def Mumbai(request):
    return render(request,'Mumbai/Mumbai.html')
def MumbaiRestaurant(request):
    rests=MumbaiRestaurants.objects.all()
    return render(request,'Mumbai/MumbaiRestaurants.html',{'rests': rests})
def PlaceMumbai(request):
    rests=PlacesMumbai.objects.all()
    return render(request,'Mumbai/PlacesMumbai.html',{'rests': rests})
def EventMumbai(request):
    rests=EventsMumbai.objects.all()
    return render(request,'Mumbai/EventsMumbai.html',{'rests': rests})
def ShopMumbai(request):
    rests=ShopsMumbai.objects.all()
    return render(request,'Mumbai/ShopsMumbai.html',{'rests': rests})
def Chennai(request):
    return render(request,'Chennai/Chennai.html')
def ChennaiRestaurant(request):
    rests=ChennaiRestaurants.objects.all()
    return render(request,'Chennai/ChennaiRestaurants.html',{'rests': rests})
def PlaceChennai(request):
    rests=PlacesChennai.objects.all()
    return render(request,'Chennai/PlacesChennai.html',{'rests': rests})
def EventChennai(request):
    rests=EventsChennai.objects.all()
    return render(request,'Chennai/EventsChennai.html',{'rests': rests})
def ShopChennai(request):
    rests=ShopsChennai.objects.all()
    return render(request,'Chennai/ShopsChennai.html',{'rests': rests})
def Kolkata(request):
    return render(request,'Kolkata/Kolkata.html')
def KolkataRestaurant(request):
    rests=KolkataRestaurants.objects.all()
    return render(request,'Kolkata/KolkataRestaurants.html',{'rests': rests})
def PlaceKolkata(request):
    rests=PlacesKolkata.objects.all()
    return render(request,'Kolkata/PlacesKolkata.html',{'rests': rests})
def EventKolkata(request):
    rests=EventsKolkata.objects.all()
    return render(request,'Kolkata/EventsKolkata.html',{'rests': rests})
def ShopKolkata(request):
    rests=ShopsKolkata.objects.all()
    return render(request,'Kolkata/ShopsKolkata.html',{'rests': rests})
def faq(request):
    return render(request,'Delhi/faq.html')
def faq(request):
    return render(request,'Mumbai/faq.html')
def faq(request):
    return render(request,'Chennai/faq.html')
def faq(request):
    return render(request,'Kolkata/faq.html')


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message   = request.POST['message']
        return render(request,"HomePage/contact.html",{'message_name':message_name})
    else:
        return render(request,"HomePage/contact.html",{})