from django.http import HttpResponse

from .models import Movie


def index(request):
    latest_movie_list = Movie.objects.order_by('-datetime_added')[:5]
    output = ', '.join([movie.title for movie in latest_movie_list])
    return HttpResponse(output)
