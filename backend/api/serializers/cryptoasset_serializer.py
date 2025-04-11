from rest_framework import serializers
from api.models import CryptoAsset

class CryptoassetSerializer(serializers.ModelSerializer):
    model = CryptoAsset
    fields = '__all__'
