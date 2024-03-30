from django.urls import path
from Computers.views import *
app_name='something'
urlpatterns=[
    path('MacBook/',MacBook,name='MacBook'),
]