# Generated by Django 4.0.4 on 2022-05-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_alter_book_external_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='external_id',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
