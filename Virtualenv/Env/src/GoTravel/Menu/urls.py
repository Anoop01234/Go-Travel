from django.urls import path
from . import views

app_name='Menu'

urlpatterns =[
    path('menu/',views.MenuPageView.as_view(),name='menu'),
    #path('menu/',views.MenuPage,name='menu'), """Function based Views"""
]
