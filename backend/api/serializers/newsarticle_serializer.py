from rest_framework import serializers
from api.models import NewsArticle

class NewsarticleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = NewsArticle
        fields = '__all__'