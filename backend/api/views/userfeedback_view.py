from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from models import UserFeedback
from serializers.userfeedback_serializer import UserfeedbackSerializer

class UserfeedbackViewSet(viewsets.ModelViewSet):
    queryset = UserFeedback.objects.all()
    serializer_class=UserfeedbackSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        feedback_type = self.request.get_params('feedback_type')

        if feedback_type:
            queryset = queryset.filter(queryset=queryset)

        return queryset