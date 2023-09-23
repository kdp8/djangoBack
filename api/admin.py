from django.contrib import admin
from .models import Actor, Address, Category, City, Country, Customer, Film, FilmActor, FilmCategory, FilmText, Inventory, Language, Payment,Rental,Staff,Store

# Register your models here.
admin.site.register(Actor)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Customer)
admin.site.register(Film)
admin.site.register(FilmActor)
admin.site.register(FilmCategory)
admin.site.register(FilmText)
admin.site.register(Inventory)
admin.site.register(Language)
admin.site.register(Payment)
admin.site.register(Rental)
admin.site.register(Staff)
admin.site.register(Store)
