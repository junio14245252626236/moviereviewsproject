import json
from django.core.management.base import BaseCommand
from movie.models import Movie
from django.utils.timezone import make_aware
from datetime import datetime

class Command(BaseCommand):
    help = "Carga hasta 100 películas desde movies.json a la base de datos"

    def handle(self, *args, **kwargs):
        try:
            # Abrimos el JSON
            with open("movie/management/commands/movies.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            # Nos quedamos solo con 100
            data = data[:100]

            movies = []
            for item in data:
                # Convertimos released en fecha aware si existe
                released = None
                if item.get("released"):
                    try:
                        released = datetime.strptime(item["released"], "%Y-%m-%d")
                        released = make_aware(released)
                    except Exception:
                        pass

                # Convertimos lastupdated en fecha aware si existe
                lastupdated = None
                if item.get("lastupdated"):
                    try:
                        naive_date = datetime.strptime(item["lastupdated"], "%Y-%m-%d %H:%M:%S.%f")
                        lastupdated = make_aware(naive_date)
                    except Exception:
                        pass

                movies.append(Movie(
                    imdbID=item.get("imdbID", ""),
                    title=item.get("title", ""),
                    year=item.get("year", ""),
                    rating=item.get("rated"),
                    runtime=item.get("runtime"),
                    genre=", ".join(item.get("genres", [])) if isinstance(item.get("genres"), list) else item.get("genre"),
                    released=released,
                    director=", ".join(item.get("directors", [])) if isinstance(item.get("directors"), list) else item.get("director"),
                    writer=", ".join(item.get("writers", [])) if isinstance(item.get("writers"), list) else item.get("writer"),
                    cast=", ".join(item.get("cast", [])) if isinstance(item.get("cast"), list) else item.get("cast"),
                    metacritic=item.get("metacritic"),
                    imdbRating=item.get("imdb", {}).get("rating") if isinstance(item.get("imdb"), dict) else item.get("imdbRating"),
                    imdbVotes=item.get("imdb", {}).get("votes") if isinstance(item.get("imdb"), dict) else item.get("imdbVotes"),
                    poster=item.get("poster"),
                    plot=item.get("plot"),
                    fullplot=item.get("fullplot"),
                    language=", ".join(item.get("languages", [])) if isinstance(item.get("languages"), list) else item.get("language"),
                    country=", ".join(item.get("countries", [])) if isinstance(item.get("countries"), list) else item.get("country"),
                    awards=item.get("awards"),
                    lastupdated=lastupdated,
                    type=item.get("type")
                ))

            # Insertamos todo de una vez
            Movie.objects.bulk_create(movies, ignore_conflicts=True, batch_size=100)

            self.stdout.write(self.style.SUCCESS("✅ Se cargaron 100 películas en la base de datos"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ocurrió un error: {e}"))
