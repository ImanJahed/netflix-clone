from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Movie(models.Model):
    class TypeMovie(models.TextChoices):
        series = 'Series'
        Film = 'Film'

    movie_id = models.UUIDField(default=uuid.uuid4())
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.ManyToManyField('Genre', related_name='movie_genre')
    type_movie = models.CharField(max_length=10, choices=TypeMovie.choices)
    length = models.CharField(max_length=12)

    release_date = models.DateField()

    movie_image = models.ImageField(upload_to='image_movie/%Y/%m/%d')
    movie_poster = models.ImageField(upload_to='poster_movie/%Y/%m/%d')
    movie_video = models.FileField(upload_to='video/%Y/%m/%d')

    movie_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ListMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_list')

    def __str__(self):
        return self.movie.title
