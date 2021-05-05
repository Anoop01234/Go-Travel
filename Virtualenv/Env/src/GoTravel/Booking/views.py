from django.shortcuts import render
from .models import EventBook,TableBook
from datetime import datetime

def EventBooking(request):
    if request.method=='POST' and request.FILES['image']:
        date=request.POST['date']
        date=datetime.strptime(date,'%d %B %Y')
        start_time=request.POST['start_time']
        end_time=request.POST['end_time']
        number_ticket=request.POST['number_ticket']
        cost_per_ticket=request.POST['cost_per_ticket']
        limit_per_person=request.POST['limit_per_person']
        event_name=request.POST['event_name']
        event_description=request.POST['event_description']
        image=request.FILES['image']
        event_book=EventBook(date=date,start_time=start_time,end_time=end_time,
                            number_ticket=number_ticket,cost_per_ticket=cost_per_ticket,
                            limit_per_person=limit_per_person,event_name=event_name,
                            event_description=event_description,image=image)
        event_book.save()
        context={'messages':'Thank you for your reservation.'}
        return render(request,'event.html',context)
    else:
        return render(request,'event.html',{})

def TableBooking(request):
    if request.method=="POST":
        date=request.POST['date']
        date=datetime.strptime(date,'%d %B %Y')
        time=request.POST['time']
        person=request.POST['person']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        occasion=request.POST['occasion']
        special_request=request.POST['special_request']
        table_book=TableBook(date=date,time=time,person=person,
                    name=name,email=email,phone=phone,
                    occasion=occasion,special_request=special_request)
        table_book.save()
        context={'messages':'Thank you for your reservation.'}
        return render(request,'table.html',context)
    else:
        return render(request,'table.html',{})
