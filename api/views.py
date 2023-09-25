from rest_framework.generics import ListAPIView
from .models import Actor, Film
from .serializers import TopRentedMoviesSerializer, TopActorsSerializer
from django.db.models import Count

class TopRentedMoviesAPIView(ListAPIView):
    serializer_class = TopRentedMoviesSerializer
    def get_queryset(self):
        queryset = Film.objects.annotate(rented=Count('inventory__rental')) \
            .order_by('-rented')[:5]
        return queryset

class TopActorsAPIView(ListAPIView):
    serializer_class = TopActorsSerializer

    def get_queryset(self):
        queryset = Actor.objects.annotate(film_count=Count('filmactor__film')) \
            .order_by('-film_count')[:5]
        return queryset

class TopRentedMoviesForActorAPIView(ListAPIView):
    serializer_class = TopRentedMoviesSerializer

    def get_queryset(self):
        actor_id = self.kwargs['actor_id'] 
        queryset = Film.objects.filter(filmactor__actor_id=actor_id) \
            .annotate(rented=Count('inventory__rental')) \
            .order_by('-rented')[:5]
        return queryset