from django.urls import path
from . import views

app_name='about'


urlpatterns=[
    path('about/',views.AboutPageView.as_view(),name='about'),
    #path('about/',views.AboutPage,name='about') """Function based Views"
]
