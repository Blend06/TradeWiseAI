from rest_framework import serializers
from api.models import UserFeedback

class UserfeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedback
        fields = '__all__'
