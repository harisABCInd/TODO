from rest_framework import permissions
from core.models import Group

class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to give access to admin or read only
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.group and request.user.group.name == 'Admin':
                return True
            if request.method in permissions.SAFE_METHODS and request.user.id == obj.id:
                return True
        return False
    