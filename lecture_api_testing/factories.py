import factory

from .models import City, Student, School


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student


class SchoolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = School
