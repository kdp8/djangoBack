from rest_framework.generics import ListAPIView
from rest_framework import generics, filters
from .models import Actor, Film, Customer
from django.db.models import Count
from .serializers import TopRentedMoviesSerializer, TopActorsSerializer, FilmSerializer, CustomerSerializer

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

class FilmSearchAPIView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'filmactor__actor__first_name', 'filmactor__actor__last_name', 'filmcategory__category__name']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer_id', 'first_name', 'last_name']