from django.urls import path
from app2.views import *
app_name='vinny'
urlpatterns=[
    path('vinny/',vinny,name='vinny'),
]