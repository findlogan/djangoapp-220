from django.shortcuts import render
from .models import Beer, Coffee, Sandwhiches, Merchandise

# Create your views here.

def home(request):
    sandwhichess = Sandwhiches.objects.all()
    return render(request, 'home.html', {'sandwhichess': sandwhichess})


def beer(request):
    beers = Beer.objects.all()
    return render(request, 'beer.html', {'beers': beers})
    
def coffee(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffee.html', {'coffees': coffees})
    
def catering(request):
    return render(request, 'catering.html')

def application(request):
    return render(request, 'application.html')

def store(request):
    merchandises = Merchandise.objects.all()
    return render(request, 'store.html', {'merchandises': merchandises})