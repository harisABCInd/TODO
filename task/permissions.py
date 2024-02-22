from rest_framework import permissions
from core.models import Group

class IsAdminOwnerOrAssignedReadOnly(permissions.BasePermission):
    """
    Custom permission to give access to admin or owner and read only access to assigned user
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if view.action != 'list' or request.user.group and request.user.group.name == 'Admin':
                return True
        return False
        

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.group and request.user.group.name == 'Admin':
                return True
            elif request.method in permissions.SAFE_METHODS and request.user.group and request.user.group.name == 'Employee' and request.user.id == obj.assigned_to:
                return True
            elif  request.user.id == obj.created_by:
                return True
        return False
    