# movie/models.py
from django.db import models

class Movie(models.Model):
    imdbID = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    rating = models.CharField(max_length=255, null=True, blank=True)
    runtime = models.CharField(max_length=50, null=True, blank=True)
    genre = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(
        upload_to="movie/images/",
        default="movie/images/default.jpg",
        blank=True
    )
    released = models.DateTimeField(null=True, blank=True)  # si lo pasaste a aware, mejor DateTimeField
    director = models.CharField(max_length=255, null=True, blank=True)
    writer = models.CharField(max_length=255, null=True, blank=True)
    cast = models.CharField(max_length=255, null=True, blank=True)
    metacritic = models.CharField(max_length=255, null=True, blank=True)
    imdbRating = models.FloatField(null=True, blank=True)
    imdbVotes = models.FloatField(null=True, blank=True)
    poster = models.URLField(null=True, blank=True)
    plot = models.TextField(null=True, blank=True)
    fullplot = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    awards = models.CharField(max_length=255, null=True, blank=True)
    lastupdated = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title
