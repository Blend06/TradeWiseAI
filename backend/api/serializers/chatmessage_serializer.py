from rest_framework import serializers
from models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['ChatMessageId', 'user', 'session_id', 'message', 'is_user_message', 'timestamp']
