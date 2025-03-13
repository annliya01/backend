from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    status = serializers.ChoiceField(choices=["Pending", "Completed"])
    deadline = serializers.DateTimeField(required=False, allow_null=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description' 'status', 'deadline', 'created_at', 'updated_at']
