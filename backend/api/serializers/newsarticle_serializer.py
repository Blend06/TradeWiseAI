from rest_framework import serializers
from models import NewsArticle

class NewsarticleSerializer(serializers.ModelSerializer):
    model = NewsArticle
    fields = '__all__'