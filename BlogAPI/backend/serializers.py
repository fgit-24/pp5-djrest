from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField()
#     slug = serializers.SlugField(max_length=200)
#     published = serializers.DateTimeField(read_only=True)


#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
    
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('title', instance.title)
#         instance.slug = validated_data.get('title', instance.title)
#         instance.published = validated_data.get('title', instance.title)
#         instance.save()
#         return instance
