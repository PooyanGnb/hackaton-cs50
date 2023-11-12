from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def listings_index(request):
    return render(request, 'listings/listings.html')

def listings_property(request):
    return render(request, 'listings/product-details.html')

