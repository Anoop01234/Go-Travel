from django.urls import path
from . import views

app_name='Home'

urlpatterns=[
    #path('',views.IndexPageView.as_view(),name='index'),
    path('index',views.IndexPage,name='index'),
]
