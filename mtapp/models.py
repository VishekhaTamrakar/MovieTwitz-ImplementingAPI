from django.db import models
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    release_date = models.DateField(null=True)
    imdb_id = models.CharField(max_length=20)
    genre = models.CharField(max_length=50)
    directed_by = models.CharField(max_length=50)
    runtime = models.IntegerField(blank=False)
    notable_casts = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    disc_price = models.DecimalField(max_digits=5, decimal_places=2)
    review = models.TextField()
    #audit fields
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.name)