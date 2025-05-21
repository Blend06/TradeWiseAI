from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from api.models import UserFeedback
from api.serializers.userfeedback_serializer import UserfeedbackSerializer  

class UserfeedbackViewSet(viewsets.ModelViewSet):
    queryset = UserFeedback.objects.all()  
    serializer_class = UserfeedbackSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        feedback_type = self.request.query_params.get('feedback_type')

        if feedback_type:
            queryset = queryset.filter(feedback_type=feedback_type)

        return queryset
