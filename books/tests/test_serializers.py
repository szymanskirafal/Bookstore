from books.models import Book
from books.serializers import BookSerializer

import pytest


@pytest.mark.django_db
def test_serializer_has_required_fields():
    book = Book.objects.create(
        title="some tilte",
        authors=["first author", "second author"],
        published_year=1999,
        acquired=False,
    )
    serializer = BookSerializer(instance=book)
    data = serializer.data
    assert set(data.keys()) == set(
        [
            "id",
            "external_id",
            "title",
            "authors",
            "published_year",
            "acquired",
            "thumbnail",
        ]
    )
