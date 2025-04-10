from django.db import models
from django.conf import settings 

class UserFeedback(models.Model):
    FEEDBACK_CHOICES = [
        ('suggestion', 'Suggestion'),
        ('problem', 'Problem'),
        ('comment', 'Comment'),
    ]
    UserFeedbackId = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.feedback_type}"