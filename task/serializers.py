from rest_framework import serializers

from core.models import Task
from user.serializers import UserDetailSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'completion_date',)

class TaskDetailSerializer(TaskSerializer):
    created_by = UserDetailSerializer()
    assigned_to = UserDetailSerializer()