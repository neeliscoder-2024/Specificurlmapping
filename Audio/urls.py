from django.urls import path
from Audio.views import *
app_name='something'
urlpatterns=[
    path('Truewireless/',Truewireless,name='Truewireless'),
]