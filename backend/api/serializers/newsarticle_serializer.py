from rest_framework import serializers
from api.models import NewsArticle

class NewsarticleSerializer(serializers.ModelSerializer):
    model = NewsArticle
    fields = '__all__'