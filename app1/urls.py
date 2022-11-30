from django.urls import path
from app1.views import *
app_name='honey'
urlpatterns=[
    path('honey/',honey,name='honey'),
]