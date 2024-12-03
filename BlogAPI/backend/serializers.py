from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    slug = serializers.SlugField(max_length=200, unique=True)
    published = serializers.DateTimeField(read_only=True)