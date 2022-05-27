from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import Book
from .serializers import BookSerializer

class ProductFilter(filters.FilterSet):
    published_after = filters.NumberFilter(field_name="published_year", lookup_expr='gte')
    published_before = filters.NumberFilter(field_name="published_year", lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['title']

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
