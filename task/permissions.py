from rest_framework import permissions
from core.models import Group

class IsAdminOwnerOrAssignedReadOnly(permissions.BasePermission):
    """
    Custom permission to give access to admin or owner and read only access to assigned user
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.group:
                if request.user.group.name == 'Admin':
                    return True
                elif request.user.group.name == 'Manager' and request.user == obj.created_by:
                    return True
                elif request.user.group.name == 'Employee' and request.method in permissions.SAFE_METHODS and request.user == obj.assigned_to:
                    return True
        return False
    

class CanUpdateTaskStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.group:
                if request.user.group.name == 'Admin':
                    return True
                elif request.user == obj.created_by or request.user == obj.assigned_to:
                    return True
        return False
