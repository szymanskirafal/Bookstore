from rest_framework import serializers
from .models import Book


class BookListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        books = []
        for item in validated_data:
            book, created = Book.objects.update_or_create(
                external_id=item['external_id'],
                defaults={
                    'external_id': item['external_id'],
                    'title': item['title'],
                    'authors': item['authors'],
                    'published_year': item['published_year'],
                    'thumbnail': item['thumbnail'],
                    },)
            books.append(book)
        return books


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            "id",
            "external_id",
            "title",
            "authors",
            "published_year",
            "acquired",
            "thumbnail",
        ]
        list_serializer_class = BookListSerializer


class ImportSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=200, allow_blank=False, allow_null=False)
