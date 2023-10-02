from django.urls import path
from . import views

urlpatterns = [
    path('top-rented-movies/', views.TopRentedMoviesAPIView.as_view(), name='top-rented-movies'),
    path('top-actors/', views.TopActorsAPIView.as_view(), name='top-actors'),
    path('top-actors/<int:actor_id>/top-rented-movies/', views.TopRentedMoviesForActorAPIView.as_view(), name='top-rented-movies-for-actor'),
    path('film-search/', views.FilmSearchAPIView.as_view(), name='film-search'),
    path('customers/create/', views.CustomerCreateView.as_view(), name='customer-create'),    
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/update/', views.CustomerUpdateAPIView.as_view(), name='customer-update'),
    path('customers/<int:pk>/delete/', views.CustomerDeleteAPIView.as_view(), name='customer-delete'),
]