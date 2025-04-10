from rest_framework import serializers
from models import WatchList

class WatchlistSerializer(serializers.ModelSerializer):
    model = WatchList
    fields = '__all__'