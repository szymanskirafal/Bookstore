# Generated by Django 4.0.4 on 2022-05-28 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_book_published_year'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='book',
            name='unique title - authors',
        ),
    ]