from rest_framework import serializers
from api.models import WatchList

class WatchlistSerializer(serializers.ModelSerializer):
    model = WatchList
    fields = '__all__'