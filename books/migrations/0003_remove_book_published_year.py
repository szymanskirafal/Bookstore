# Generated by Django 4.0.4 on 2022-05-26 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_book_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_year',
        ),
    ]
