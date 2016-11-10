from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=250, unique_for_year="release_date")
    release_date = models.DateField('Release Date')
    runtime = models.PositiveSmallIntegerField()
    cover_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', height_field=256, width_field=192)
    summary = models.TextField()

    FORMAT_CHOICES = (
        ('BRD', 'BRD'),
        ('DVD', 'DVD'),
        ('VHS', 'VHS'),
    )
    format = models.CharField(
        max_length = 3,
        choices = FORMAT_CHOICES,
        default = 'BRD'
    )

    datetime_added = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title + " (" + str(self.release_date.year) + ")"