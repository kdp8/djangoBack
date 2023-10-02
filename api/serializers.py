from rest_framework import serializers
from .models import Film, Actor, Customer

class TopRentedMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film 
        fields = '__all__' 

class TopActorsSerializer(serializers.ModelSerializer):
    film_count = serializers.IntegerField()
    class Meta:
        model = Actor
        fields = ('actor_id', 'first_name', 'last_name', 'film_count')

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {
            'customer_id': {'read_only': True},
        }