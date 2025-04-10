from rest_framework import serializers
from models import User

class UserSerialzier(serializers.ModelSerializer):
    model = User
    fields =  fields = ['id', 'username', 'email', 'is_staff', 'is_active']