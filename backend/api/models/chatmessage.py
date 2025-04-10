from django.db import models
from django.conf import settings 

class ChatMessage(models.Model):
    ChatMessageId = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    is_user_message = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{'User' if self.is_user_message else 'AI'}: {self.message[:30]}"