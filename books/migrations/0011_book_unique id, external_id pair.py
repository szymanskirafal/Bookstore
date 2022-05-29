# Generated by Django 4.0.4 on 2022-05-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_remove_book_unique title - authors'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('id', 'external_id'), name='unique id, external_id pair'),
        ),
    ]
