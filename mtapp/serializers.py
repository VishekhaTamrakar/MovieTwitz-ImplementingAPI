from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'name', 'release_date', 'imdb_id', 'poster', 'genre', 'directed_by', 'runtime', 'notable_casts', 'rating', 'review')