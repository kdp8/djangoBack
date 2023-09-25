from django.urls import path
from . import views

urlpatterns = [
    path('top-rented-movies/', views.TopRentedMoviesAPIView.as_view(), name='top-rented-movies'),
    path('top-actors/', views.TopActorsAPIView.as_view(), name='top-actors'),
    path('top-actors/<int:actor_id>/top-rented-movies/', views.TopRentedMoviesForActorAPIView.as_view(), name='top-rented-movies-for-actor'),
]