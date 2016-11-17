from django.views import generic
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate, login


from .models import Movie, Collection


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_movie_list'

    def get_queryset(self):
        return Movie.objects.order_by('-datetime_added')[:5]


class DetailView(generic.DetailView):
    model = Movie
    template_name = 'detail.html'

    def get_queryset(self):
        return Movie.objects


class CollectionView(generic.DetailView):
    model = Collection
    template_name = 'collection.html'

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            return Collection.objects.filter(user=self.request.user)


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)