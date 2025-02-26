from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskListSerializer(serializers.ModelSerializer):
    short_description = serializers.SerializerMethodField() # since we want to list all the tasks we shorten the description

    class Meta:
        model = Task
        fields = ['title', 'short_description', 'due_date', 'priority', 'status']

    def get_short_description(self, instance):
        # Truncate the description to 30 characters, and add "..." if it's longer
        if len(instance.description) > 30:
            return instance.description[:30] + '...'
        return instance.description
    

class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'status', 'completed_at']
    
class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']

    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the paset. Please correct the due date value.")
        return value
    
    def validate_titel(self, value):
        if Task.objects.filter(tietle = value).exists(): # to insure the uniquness of the title
            raise serializers.ValidationError("The provided title is already in use. Please select diffrent title.")
        return value
    
    def create(self, validated_data):
        user = self.context['request'].user # to assign the user field on task model the current user
        return Task.objects.create(user = user, **validated_data)

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = fields = ['title', 'description', 'due_date', 'priority', 'status']

    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the paset. Please correct the due date value.")
        return value
    
    def validate_titel(self, value):
        request = self.context.get('request')
        if request:
            current_title = request.parser_context['kwargs']['title']
            if Task.objects.exclude(title = current_title).filter(tietle = value).exists(): # to exclude the title of the task being updated from being detected
                raise serializers.ValidationError("The provided title is already in use. Please select diffrent title.")
        return value
    
    def update(self, instance, validated_data):
        if 'status' in validated_data and validated_data['status'] == 'Completed': # if the task has been marked as completed it assigns the time of completion for completed at field
            instance.completed_at = timezone.now()
        return super().update(instance, validated_data)









































