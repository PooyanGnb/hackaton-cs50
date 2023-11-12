from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def faq(request):
    return render(request, 'core/faq.html')

def service(request):
    return render(request, 'core/service.html')