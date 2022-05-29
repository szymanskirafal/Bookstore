from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

import requests

from .filters import BookFilter
from .models import Book
from .serializers import BookSerializer, BookImportSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


class ImportCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookImportSerializer

    def create(self, request, *args, **kwargs):
        author = self.request.query_params.get('authors')
        google_books_url = 'https://www.googleapis.com/books/v1/volumes?q=author:'
        author = str(author)
        url = google_books_url+author
        response = requests.get(url)
        response = response.json()
        data = []
        for item in response['items']:
            d = {}
            d['external_id'] = item['id']
            d['title'] = item['volumeInfo']['title']
            d['authors'] = item['volumeInfo']['authors']
            d['published_year'] = item['volumeInfo']['publishedDate'][0:4]
            for k,v in item['volumeInfo'].items():
                if k == 'imageLinks':
                    d['thumbnail'] = v['thumbnail']
                    data.append(d)
        serializer = BookSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        books_imported = len(response['items'])
        dict_books_imported = {'imported': books_imported}
        return Response(dict_books_imported, status=status.HTTP_201_CREATED, headers=headers)
