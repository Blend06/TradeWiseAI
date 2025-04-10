from rest_framework import serializers
from models import UserFeedback

class UserfeedbackSerializer(serializers.ModelSerializer):
    model = UserFeedback
    fields = '__all__'