from django.db import models

class Book(models.Model):
    external_id = models.CharField(blank=True, max_length=300)
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    published_year = models.PositiveSmallIntegerField()
    acquired = models.BooleanField(default=False)
    thumbnail = models.URLField(blank=True)

    def __str__(self):
        return f"Book - {self.title} - {self.authors}"
