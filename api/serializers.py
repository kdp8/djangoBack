from rest_framework import serializers
from .models import Film, Actor

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