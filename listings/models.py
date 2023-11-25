from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify


class Province(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Property(models.Model):
    PROPERTY_TYPES = [
        ('مسکونی آپارتمان', 'مسکونی آپارتمان'),
        ('مسکونی ویلایی', 'مسکونی ویلایی'),
        ('تجاری', 'تجاری'),
        ('صنعتی', 'صنعتی'),
        ('کشاورزی', 'کشاورزی'),
    ]

    CONTRACT_TYPES = [
        ('فروشی', 'فروشی'),
        ('اجاره', 'اجاره'),
        ('رهن کامل', 'رهن کامل')
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True, allow_unicode=True)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    square_m = models.IntegerField()
    built_date = models.SmallIntegerField(validators=[MinValueValidator(1350), MaxValueValidator(1420)], null=True, blank=True)
    type_of_property = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    type_of_contract = models.CharField(max_length=10, choices=CONTRACT_TYPES)
    price = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000000000)])
    rent = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(250000000)], blank=True, null=True)
    counted_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)

    class Meta:
            ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Automatically generate the slug before saving
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    #automatically increases number of vieww
    def view_increament(self):
        self.counted_views += 1
        self.save()

    @property
    def contract_count(self):
        return Property.objects.filter(type_of_contract=self.type_of_contract)
        
    @property
    def property_count(self):
        return Property.objects.filter(type_of_property=self.type_of_property)



class Property_Picture(models.Model):
    propertyid = models.ForeignKey(Property, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='property_pictures/')

    def __str__(self):
        return f'Picture for {self.propertyid.name}'
    

class Property_properties(models.Model):
    propertyid = models.ForeignKey(Property, on_delete=models.CASCADE)
    rooms = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True, blank=True)
    baths = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True, blank=True)
    parking = models.BooleanField(default=False, null=True, blank=True)
    floor = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(15)], null=True, blank=True)
    pool = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f'Property of {self.propertyid.name}'
    
    # a function to make numbers into boolean. if it is True, it will show دارد and otherwise it will show ندارد
    def num_to_bool(self, property):
        if getattr(self, property):
            return 'دارد'
        else:
            return 'ندارد'
        
    # a function to null to 0
    def null_to_zero(self, property):
        if not getattr(self, property):
            return '0'
        else:
            return getattr(self, property)
