from django_filters import rest_framework as filters
from .models import Book


class ProductFilter(filters.FilterSet):
    published_after = filters.NumberFilter(field_name="published_year", lookup_expr='gte')
    published_before = filters.NumberFilter(field_name="published_year", lookup_expr='lte')
    author = filters.CharFilter(field_name='authors', lookup_expr='contains')
    class Meta:
        model = Book
        fields = ['title', 'acquired', ]
