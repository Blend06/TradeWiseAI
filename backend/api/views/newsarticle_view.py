from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from models import NewsArticle
from serializers.newsarticle_serializer import NewsarticleSerializer

class NewsarticleViewSet(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsarticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        source = self.request.query_params.get('source')
        
        if source:
            queryset = queryset.filter(source=source)
    
        return queryset

   
