from django.shortcuts import render
from rest_framework import viewsets
from core.models import Task
from task.permissions import IsAdminOwnerOrAssignedReadOnly
from task.serializers import TaskDetailSerializer, TaskSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_class = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOwnerOrAssignedReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskDetailSerializer
        
        return self.serializer_class
