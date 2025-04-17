from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import User
from api.serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        is_active = self.request.query_params.get('is_active')
        is_staff = self.request.query_params.get('is_staff')

        if is_active is not None:
            queryset = queryset.filter(is_active=(is_active.lower() == 'true'))
        
        if is_staff is not None:
            queryset = queryset.filter(is_staff=(is_staff.lower() == 'true'))

        return queryset

    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)