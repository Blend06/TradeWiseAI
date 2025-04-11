from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import WatchList
from api.serializers.watchlist_serializer import WatchlistSerializer

class WatchlistViewSet(viewsets.ModelViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = super().get_queryset()
        
        user = self.request.query_params.get('user')

        
        if user:
            queryset = queryset.filter(user__Userid=user)
        
        return queryset