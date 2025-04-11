from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields =  fields = ['id', 'username', 'email', 'is_staff', 'is_active']