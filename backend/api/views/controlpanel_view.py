from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

class ControlPanelView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({
            'total_users' : User.objects.count(),
        })