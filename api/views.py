from rest_framework.generics import ListAPIView
from rest_framework import generics, filters, serializers
from .models import Actor, Film, Customer, Rental
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomerWithRentedMoviesSerializer, TopRentedMoviesSerializer, TopActorsSerializer, FilmSerializer, CustomerSerializer

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

class CustomerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'address', 'active', 'last_update')

class CustomerUpdateAPIView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerUpdateSerializer

class CustomerDeleteAPIView(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer_id', 'first_name', 'last_name']

class CustomerRentedMoviesAPIView(APIView):
    
    def get(self, request, customer_id):
        try:
            customer = Customer.objects.get(customer_id=customer_id)
        except Customer.DoesNotExist:
            return Response({"message": "Customer not found"}, status=404)

        rentals = Rental.objects.filter(customer=customer)
        rented_movies = []
        for rental in rentals:
            inventory = rental.inventory
            film = inventory.film
            rented_movies.append({
                "film_title": film.title,
                "rental_date": rental.rental_date,
                "return_date": rental.return_date,
            })

        return Response({"customer": customer.first_name, "rented_movies": rented_movies})

class CustomerWithRentedMoviesAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerWithRentedMoviesSerializer