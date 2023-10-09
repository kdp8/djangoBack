from django.test import TestCase
from api.models import Country, City

class CountryModelTest(TestCase):
    def test_country_str_method(self):
        country = Country.objects.create(country="Test Country")
        self.assertEqual(str(country), "Test Country")

    def test_country_cities(self):
        country = Country.objects.create(country="Test Country")
        city1 = City.objects.create(city="City A", country=country)
        city2 = City.objects.create(city="City B", country=country)
        cities = country.city_set.all()
        self.assertEqual(list(cities), [city1, city2])

class CityModelTest(TestCase):
    def test_city_str_method(self):
        country = Country.objects.create(country="Test Country")
        city = City.objects.create(city="Test City", country=country)
        self.assertEqual(str(city), "Test City, Test Country")

    def test_city_update(self):
        country = Country.objects.create(country="Test Country")
        city = City.objects.create(city="Test City", country=country)
        city.city = "Updated City"
        city.save()
        updated_city = City.objects.get(pk=city.pk)
        self.assertEqual(updated_city.city, "Updated City")

    def test_country_deletion(self):
        country = Country.objects.create(country="Test Country")
        country.delete()
        with self.assertRaises(Country.DoesNotExist):
            Country.objects.get(pk=country.pk)