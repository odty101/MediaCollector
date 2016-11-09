from django.views import generic

from .models import Movie


class IndexView(generic.ListView):
    template_name = 'Movies/index.html'
    context_object_name = 'latest_movie_list'

    def get_queryset(self):
        """Return the last five added moviees."""
        return Movie.objects.order_by('-datetime_added')[:5]


class DetailView(generic.DetailView):
    model = Movie
    template_name = 'Movies/detail.html'

    def get_queryset(self):
        return Movie.objects