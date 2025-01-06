from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def ganeshutsav(request):
    return render(request, 'ganeshutsav.html')

def shivjayanti(request):
    return render(request, 'shivjayanti.html')

def navratri(request):
    return render(request, 'navratri.html')