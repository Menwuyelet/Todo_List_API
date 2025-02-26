from .models import User
from rest_framework import serializers
import re

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, min_length=8)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'username']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("The email you provided is alredy in use. Please use different email.")
        return value
    
    def validate_username(self, value):
        if value and not re.match(r'^[A-Za-z0-9_]+$', value):
            raise serializers.ValidationError("Username can only contain letters, numbers, and underscores.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            username=validated_data.get('username', '') # if user name is not provided it sets it to blank
        )
        return user
    
class UpdateProfile(serializers.ModelSerializer):
    current_password = serializers.CharField(write_only = True, required = True)
    new_password = serializers.CharField(write_only = True, min_length = 8, required = False)

    class Meta:
        model = User
        fields = ['username', 'email', 'current_password', 'new_password']

    def validate(self, data):
        user = self.instance

        if 'new_password' in data and data['new_password']:
            if not user.check_password(data['current_password']):
                raise serializers.ValidationError({'current_password': 'Current password is incorrect.'})
            
        return data
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('emil', instance.email)
        instance.username = validated_data.get('username', instance.username)

        if 'new_password' in validated_data and validated_data['new_password']:
            instance.set_password(validated_data['new_password'])

        instance.save()
        return instance
    