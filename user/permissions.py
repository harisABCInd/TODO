from rest_framework import permissions
from core.models import Group

class IsAdminOrOwnerReadOnly(permissions.BasePermission):
    """
    Custom permission to give access to admin or owner read only
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if view.action == 'retrieve' or request.user.group and request.user.group.name == 'Admin':
                return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.group and request.user.group.name == 'Admin':
                return True
            if view.action == 'retrieve' and request.user.id == obj.id:
                return True
        return False