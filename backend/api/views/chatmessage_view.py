from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models import ChatMessage
from api.serializers.chatmessage_serializer import ChatMessageSerializer
from rest_framework import status

class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    # Krijimi i mesazheve
    def perform_create(self, serializer):
        session_id = self.request.data.get('session_id')
        if session_id:
            serializer.save(session_id=session_id)
        else:
            raise serializer.ValidationError("Session ID is required")

    # Fshirja e mesazheve kur sesioni mbyllet
    @action(detail=False, methods=['delete'])
    def delete_session_messages(self, request, *args, **kwargs):
        session_id = request.data.get('session_id')
        if not session_id:
            return Response({'detail': 'Session ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Fshirja e mesazheve për sesionin përkatës
        deleted_count, _ = ChatMessage.objects.filter(session_id=session_id).delete()
        return Response({'detail': f'{deleted_count} messages deleted.'}, status=status.HTTP_200_OK)