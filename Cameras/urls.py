from django.urls import path
from Cameras.views import *
app_name='anything'
urlpatterns=[
    path('Canon/',Canon,name='Canon'),
]