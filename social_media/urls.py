
from django.urls import path
from social_media.views import home

urlpatterns = [

     path('home',home,name='home')
]