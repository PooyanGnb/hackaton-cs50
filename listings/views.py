from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.shortcuts import render, get_object_or_404

# Create your views here.
def listings_properties(request):
    return render(request, 'listings/listings.html')

def listings_details(request, slug):
    property = get_object_or_404(Property.objects.all(), slug=slug)
    images = Property_Picture.objects.filter(propertyid__slug=slug)
    property.view_increament()
    context = {'images': images, 'property': property}
    return render(request, 'listings/product-details.html', context)

