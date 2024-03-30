from django.urls import path
from Mobiles.views import *
app_name='anything'
urlpatterns=[
    path('Mobileaccessories/',Mobileaccessories,name='Mobileaccessories'),
]