from django.contrib import admin
from .models import *


class Property_PictureAdmin(admin.StackedInline):
    model = Property_Picture


class Property_propertiesAdmin(admin.TabularInline):
    model = Property_properties
    extra = 1


class PropertyAdmin(admin.ModelAdmin):
    inlines = [Property_propertiesAdmin, Property_PictureAdmin]
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    include = ['price_per_meter']
    list_display = ('name', 'type_of_property', 'type_of_contract', 'province', 'city', 'counted_views')
    list_filter = ('type_of_contract','type_of_property' )
    # ordering = ['-created_at']
    exclude = ('slug', 'counted_views',)
    search_fields = ['name', 'description']

    readonly_fields = ('price_per_meter',)  # Add your custom method here

    def price_per_meter(self, obj):
        # Assuming you have a square meter field named 'square_meters' in your model
        if obj.square_m:
            return f"{obj.price / obj.square_m:.0f} به ازای هر هتر"
        return "N/A"

    # calculate_price_per_meter.short_description = 'Price per meter'


admin.site.register(Property, PropertyAdmin)