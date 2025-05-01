from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Userid', 'username', 'email', 'password', 'is_active', 'is_staff']
        read_only_fields = ['Userid', 'is_active', 'is_staff']

    def create(self, validated_data):
        pwd = validated_data.pop('password')
        #this will call CustomUserManager.create_user to hash te password and save:
        user = User.objects.create_user(**validated_data, password=pwd)
        return user