from django.contrib import admin
from .models import *


class Property_PictureAdmin(admin.StackedInline):
    model = Property_Picture

class PropertyAdmin(admin.ModelAdmin):
    inlines = [Property_PictureAdmin]
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('name', 'type_of_property', 'type_of_contract', 'province', 'city', 'counted_views')
    list_filter = ('type_of_contract','type_of_property' )
    # ordering = ['-created_at']
    exclude = ('slug', 'counted_views',)
    search_fields = ['name', 'description']


admin.site.register(Property, PropertyAdmin)