from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def beer(request):
    return render(request, 'beer.html')
    
def coffee(request):
    return render(request, 'coffee.html')
    
def catering(request):
    return render(request, 'catering.html')