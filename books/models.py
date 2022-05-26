from django.db import models

class Book(models.Model):
    external_id = models.CharField(blank=True, max_length=300)
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    acquired = models.BooleanField(default=False)
    published_year = models.PositiveSmallIntegerField()
    thumbnail = models.URLField(blank=True)
