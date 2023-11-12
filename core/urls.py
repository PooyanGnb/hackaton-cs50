from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq'),
    path('service/', service, name='service'),
]