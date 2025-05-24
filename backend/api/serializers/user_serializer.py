from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(required=False)
    
    class Meta:
        model = User
        fields = ['Userid', 'username', 'email', 'password', 'is_staff']
        read_only_fields = ['Userid', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        pwd = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=pwd)
        return user

    def update(self, instance, validated_data):
        pwd = validated_data.pop('password', None)
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        if pwd:
            instance.set_password(pwd)
        instance.save()
        return instance
