from django.urls import path
from listings.views import *

app_name = 'listings'

urlpatterns = [
    path('', listings_index, name='index'),
    path('<str:slug>/', listings_property, name='property'),
]