from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.shortcuts import render, get_object_or_404

# Create your views here.
def listings_properties(request):
    property = Property.objects.all()[:20]
    property_list = list()
    for prop in property:
        firstpic = Property_Picture.objects.filter(propertyid=prop).first()
        belongings = Property_properties.objects.filter(propertyid=prop).first()
        belongings.parking = belongings.num_to_bool('parking')
        belongings.pool = belongings.num_to_bool('pool')
        belongings.rooms = belongings.null_to_zero('rooms')
        belongings.baths = belongings.null_to_zero('baths')
        property_list.append({'property': prop, 'picture': firstpic, 'belongings':belongings})
    context = {'property': property_list}
    return render(request, 'listings/listings.html', context)


def listings_details(request, slug):
    property = get_object_or_404(Property.objects.all(), slug=slug)
    images = Property_Picture.objects.filter(propertyid__slug=slug)
    belonging = Property_properties.objects.get(propertyid__slug=slug)
    belonging.parking = belonging.num_to_bool('parking')
    belonging.pool = belonging.num_to_bool('pool')
    belonging.rooms = belonging.null_to_zero('rooms')
    belonging.baths = belonging.null_to_zero('baths')
    property.view_increament()
    context = {'images': images, 'property': property, 'belonging': belonging}
    return render(request, 'listings/product-details.html', context)


def listings_search(request):
    if s := request.GET.get('s'):
        property = Property.objects.filter(name__contains=s)
        property_list = list()
        for prop in property:
            firstpic = Property_Picture.objects.filter(propertyid=prop).first()
            belongings = Property_properties.objects.filter(propertyid=prop).first()
            belongings.parking = belongings.num_to_bool('parking')
            belongings.pool = belongings.num_to_bool('pool')
            belongings.rooms = belongings.null_to_zero('rooms')
            belongings.baths = belongings.null_to_zero('baths')
            property_list.append({'property': prop, 'picture': firstpic, 'belongings':belongings})
    context = {'property': property_list}
    return render(request, 'listings/listings.html', context)