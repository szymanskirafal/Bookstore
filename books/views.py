from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import ProductFilter
from .models import Book
from .serializers import BookSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
