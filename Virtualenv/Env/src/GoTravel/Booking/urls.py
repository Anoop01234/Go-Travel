from django.urls import path
from . import views

app_name='Booking'

urlpatterns=[
    path('event/',views.EventBooking,name='event'),
    path('table/',views.TableBooking,name='table'),
]
