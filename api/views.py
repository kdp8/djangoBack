from rest_framework.generics import ListAPIView
from .models import Film
from .serializers import TopRentedMoviesSerializer
from django.db.models import Count

class TopRentedMoviesAPIView(ListAPIView):
    serializer_class = TopRentedMoviesSerializer
    def get_queryset(self):
        queryset = Film.objects.annotate(rented=Count('inventory__rental')) \
            .order_by('-rented')[:5]
        return queryset

