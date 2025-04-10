from rest_framework import serializers
from models import CryptoAsset

class CryptoassetSerializer(serializers.ModelSerializer):
    model = CryptoAsset
    fields = '__all__'
