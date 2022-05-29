from django.contrib.postgres.fields import ArrayField
from django.db import models
from books.models import Book

import pytest


class TestBook:
    def test_title_field(self):
        field = Book._meta.get_field("title")
        field_type_expected = models.CharField
        field_type_given = field.__class__
        assert field_type_expected == field_type_given
        field_max_length_expected = 500
        field_max_length_given = field.max_length
        assert field_max_length_expected == field_max_length_given

    def test_authors_field(self):
        field = Book._meta.get_field("authors")
        field_type_expected = ArrayField
        field_type_given = field.__class__
        assert field_type_expected == field_type_given

    @pytest.mark.django_db
    def test_str_return_title(self):
        book = Book.objects.create(
            title="Some title",
            authors=["Some author"],
            published_year=2000,
        )
        assert str(book) == "Book - Some title ['Some author']"
