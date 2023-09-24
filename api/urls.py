from django.urls import path
from . import views

urlpatterns = [
    path('top-rented-movies/', views.TopRentedMoviesAPIView.as_view(), name='top-rented-movies'),
]

