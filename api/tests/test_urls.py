from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import TopRentedMoviesAPIView, FilmSearchAPIView


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('top-rented-movies')
        self.assertEquals(resolve(url).func.view_class, TopRentedMoviesAPIView)

    def test_top_rented_movies_url_is_resolved(self):
        url = reverse('top-rented-movies')
        view = resolve(url).func.view_class
        self.assertIsInstance(view(), TopRentedMoviesAPIView)

    def test_customer_list_url_is_resolved(self):
        url = reverse('film-search')
        self.assertIs(resolve(url).func.view_class, FilmSearchAPIView)
