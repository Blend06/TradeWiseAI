from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import User
from api.serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):

        queryset = super().get_queryset()
        is_active = self.request.query_params.get('is_active')
        is_staff = self.request.query_params.get('is_staff')

        if is_active is not None:
            if is_active.lower() == 'true':
                queryset = queryset.filter(is_active=True)
            elif is_active.lower() == 'false':
                queryset = queryset.filter(is_active=False)
        
        if is_staff is not None:
            if is_staff.lower() == 'true':
                queryset = queryset.filter(is_staff=True)
            elif is_staff.lower() == 'false':
                queryset = queryset.filter(is_staff=False)

        return queryset