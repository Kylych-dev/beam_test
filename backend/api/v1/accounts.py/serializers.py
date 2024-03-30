# serializers.py

from rest_framework import serializers
from apps.accounts.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 
            'role', 
            'email', 
            'is_staff', 
            'is_active'
        ]
