from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.


def home(request):
 #return HttpResponse('<h1> Welcome to HOME PAGE</h1>')
 #return render(request, 'home.html')
 #return render(request, 'home.html', {'name': 'Emilton Mena'})
 searchTerm = request.GET.get('searchMovie')
 if searchTerm:
     movies = Movie.objects.filter(title__icontains=searchTerm)
 else:
    movies = Movie.objects.all() 
 return render(request, 'home.html', {'movies': movies, 'searchTerm': searchTerm})


# Página About
def about(request):
    return render(request, 'about.html', {'name': 'Emilton Mena'})
