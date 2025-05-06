from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Userid', 'username', 'email', 'password', 'is_staff']
        read_only_fields = ['Userid', 'is_active']

    def create(self, validated_data):
        pwd = validated_data.pop('password')
        #this will call CustomUserManager.create_user to hash te password and save:
        user = User.objects.create_user(**validated_data, password=pwd)
        return user
    
    def update(self, instance, validated_data):
        pwd = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if pwd:
            instance.set_password(pwd)
        instance.save()
        return instance