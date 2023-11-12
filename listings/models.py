from django.db import models
from django.core.validators import MaxValueValidator


class Province(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = [
        ('residental apartment', 'مسکونی آپارتمان'),
        ('residental villa', 'مسکونی ویلایی'),
        ('commertial', 'تجاری'),
        ('industrial', 'صنعتی'),
        ('agricultural', 'کشاورزی'),
    ]

    CONTRACT_TYPES = [
        ('sale', 'فروشی'),
        ('rent', 'اجاره'),
        ('mortgage', 'رهن کامل')
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    type_of_property = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    type_of_contract = models.CharField(max_length=10, choices=CONTRACT_TYPES)
    price = models.IntegerField(validators=[MaxValueValidator(100000000000)])
    rent = models.IntegerField(validators=[MaxValueValidator(250000000)], blank=True, null=True)
    # pictures = models.ManyToManyField('PropertyPicture', blank=True)
    counted_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)

    class Meta:
            ordering = ['-created_at']

    def __str__(self):
        return self.name
    
    def view_increament(self):
        self.counted_views += 1
        self.save()

class Property_Picture(models.Model):
    propertyid = models.ForeignKey(Property, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='property_pictures/')

    def __str__(self):
        return f'Picture for {self.property.name}'