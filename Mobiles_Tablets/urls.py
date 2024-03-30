from django.urls import path
from Mobiles_Tablets.views import *
app_name='something'
urlpatterns=[
    path('Apple/',Apple,name='Apple'),
]