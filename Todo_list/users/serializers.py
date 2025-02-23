from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
    
class UpdateProfile(serializers.ModelSerializer):
    current_password = serializers.CharField(write_only = True)
    new_password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['email', 'password']
    def validated(self, data):
        user = self.instance

        if 'new_password' in data and data['new_password']:
            if not user.check_password(data['current_password']):
                raise serializers.ValidationError({'current_password': 'Current password is incorrect.'})
            
        return data
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('emil', instance.email)

        if 'new_password' in validated_data and validated_data['new_password']:
            instance.set_password(validated_data['new_password'])

        instance.save()
        return instance
    