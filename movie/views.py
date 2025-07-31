from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
 #return HttpResponse('<h1> Welcome to HOME PAGE</h1>')
 #return render(request, 'home.html')
 return render(request, 'home.html', {'name': 'Emilton Mena'})


# Página About
def about(request):
    return HttpResponse('<h1>Welcome to ABOUT PAGE</h1>')