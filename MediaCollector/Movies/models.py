from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=250)
    release_date = models.DateField('Release Date')
    runtime = models.IntegerField()

    def __str__(self):
        return self.title + " (" + str(self.release_date.year) + ")"