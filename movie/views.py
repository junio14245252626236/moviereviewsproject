from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
import matplotlib
matplotlib.use('Agg')   # Backend no interactivo
import matplotlib.pyplot as plt
import io
import base64


def signup(request):
    email = request.GET.get("email")   
    return render(request, "signup.html", {"email": email})


def get_graph():
    """Convierte la gráfica de matplotlib en base64 para usarla en templates."""
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')
    plt.close()
    return graphic


def statistics_view(request):

    all_movies = Movie.objects.all()

    # =======================
    # 1. Gráfica: películas por año
    # =======================
    movie_counts_by_year = {}
    for movie in all_movies:
        year = movie.year if movie.year else "None"
        movie_counts_by_year[year] = movie_counts_by_year.get(year, 0) + 1

    # ✅ Ordenamos por año (importante para evitar que se mezclen)
    movie_counts_by_year = dict(sorted(movie_counts_by_year.items()))

    plt.figure(figsize=(12, 6))  # ✅ Más ancha para evitar etiquetas encima
    plt.bar(movie_counts_by_year.keys(), movie_counts_by_year.values())
    plt.title('Movies per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=60, ha="right")  # ✅ Rotar y alinear etiquetas
    plt.tight_layout()
    graphic_year = get_graph()

    # =======================
    # 2. Gráfica: películas por género (solo el primer género)
    # =======================
    movie_counts_by_genre = {}
    for movie in all_movies:
        if movie.genre:
            first_genre = movie.genre.split(",")[0].strip()
        else:
            first_genre = "None"
        movie_counts_by_genre[first_genre] = movie_counts_by_genre.get(first_genre, 0) + 1

    # ✅ Ordenamos géneros para consistencia
    movie_counts_by_genre = dict(sorted(movie_counts_by_genre.items()))

    plt.figure(figsize=(10, 6))
    plt.bar(movie_counts_by_genre.keys(), movie_counts_by_genre.values())
    plt.title('Movies per Genre (First Genre Only)')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45, ha="right")  # ✅ Mejor visibilidad
    plt.tight_layout()
    graphic_genre = get_graph()

    # Renderizar template con ambas gráficas
    return render(request, 'statistics.html', {
        'graphic_year': graphic_year,
        'graphic_genre': graphic_genre
    })


# Página principal
def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all() 
    return render(request, 'home.html', {'movies': movies, 'searchTerm': searchTerm})


# Página About
def about(request):
    return render(request, 'about.html', {'name': 'Emilton Mena'})

