from rest_framework import serializers
from .models import Book


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


class Book2Serializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            "authors",
        ]
