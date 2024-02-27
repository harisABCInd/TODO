from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets, generics
from core.models import Task, User
from task.permissions import IsAdminOwnerOrAssignedReadOnly
from task.serializers import TaskDetailSerializer, TaskSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_class = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOwnerOrAssignedReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskDetailSerializer
        
        return self.serializer_class
    
    def get_queryset(self):
        if self.request.user.group:
            group_name = self.request.user.group.name
            user = self.request.user
            if group_name == 'Admin':
                return Task.objects.all()
            elif group_name == 'Manager':
                return Task.objects.filter(assigned_to=user) | Task.objects.filter(created_by=user)
            elif group_name == 'Employee':
                return Task.objects.filter(assigned_to=user)

        return Task.objects.none() 
            

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        user_group = self.request.user.group.name
        assigned_user = serializer.validated_data.get('assigned_to')

        if user_group == 'Manager' and assigned_user.group.name == "Admin":
            raise PermissionDenied("Managers cannot assign tasks to Admins.")
        
        if user_group == 'Employee':
            raise PermissionDenied("Employees cannot assign tasks.")

        if serializer.validated_data.get('status') == 'complete':
            serializer.validated_data['completion_date'] = datetime.now()

        serializer.save(created_by=self.request.user)
    
    def perform_update(self, serializer):
        serializer.is_valid(raise_exception=True)
        instance = self.get_object()
        user_group = self.request.user.group.name
        assigned_user = instance.assigned_to

        if 'assigned_to' in serializer.validated_data:
            assigned_user = serializer.validated_data.get('assigned_to')
            if user_group == 'Manager' and assigned_user.group.name == "Admin":
                raise PermissionDenied("Managers cannot assign tasks to Admins.")

        if 'status' in serializer.validated_data and serializer.validated_data['status'] == 'complete':
            serializer.validated_data['completion_date'] = datetime.now()

        serializer.save()

class TaskStatusUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()

    
            