from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets

import requests

from .filters import ProductFilter
from .models import Book
from .serializers import BookSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ImportCreateAPIView(generics.CreateAPIView)

    def create(self, request, *args, **kwargs):
        url = https://www.googleapis.com/books/v1/volumes?q=Hobbit
        author = request.query_params
        response = requests.get(url, params=author)
        response = response.json()
        data = []
        for item in response['items']:
            d = {}
            d['external_id'] = item['id']
            d['title'] = item['volumeInfo']['title']
            d['authors'] = item['volumeInfo']['authors']
            d['published_year'] = item['volumeInfo']['publishedDate']
            d['thumbnail'] = item['volumeInfo']['imageLinks']['smallThumbnail']
            data.append(d)
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
