from rest_framework.permissions import IsAuthenticated
from api.models import CryptoAsset
from api.serializers.cryptoasset_serializer import CryptoassetSerializer
from rest_framework import viewsets

class CryptoassetViewSet(viewsets.ModelViewSet):
    
    queryset = CryptoAsset.objects.all()
    serializer_class = CryptoassetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        queryset = super().get_queryset()
        symbol = self.request.query_params.get('symbol')

        if symbol:
            queryset = queryset.filter(symbol=symbol)
        return queryset