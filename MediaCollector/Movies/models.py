from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=250, unique_for_year="release_date")
    release_date = models.DateField('Release Date')
    runtime = models.PositiveSmallIntegerField()
    cover_image = models.URLField(default="#")
    summary = models.TextField(default="Default Summary")

    FORMAT_CHOICES = (
        ('Blu-ray', 'Blu-ray'),
        ('DVD', 'DVD'),
    )
    format = models.CharField(
        max_length = 15,
        choices = FORMAT_CHOICES,
        default = 'Blu-ray'
    )
    is_ripped = models.BooleanField(default=False)

    datetime_added = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title + " (" + str(self.release_date.year) + ")"


class Genre(models.Model):
    name = models.CharField(max_length=250, unique="name")
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name