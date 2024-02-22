from rest_framework import permissions
from core.models import Group

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to give access to admin or read only
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                admin_group = Group.objects.get(name="Admin")
                return admin_group == request.user.group
            except Group.DoesNotExist:
                return False
        return False
    