from django.urls import path
from listings.views import *

app_name = 'listings'

urlpatterns = [
    path('', listings_properties, name='index'),
    path('<str:slug>/', listings_details, name='property'),
]