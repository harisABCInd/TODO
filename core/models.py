from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    group = models.OneToOneField(Group, null=True, blank=True, on_delete=models.SET_NULL, related_name='group')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        permissions = (
            ('create_user', 'Create user'),
            ('update_group', 'Update group'),
        )

    def __str__(self) -> str:
        return self.email
    

class Task(models.Model):
    name = models.CharField(max_length=128, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_by')
    assigned_to = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_to')
    choices = [
        ('in_progress', 'In progress'),
        ('complete', 'Complete'),
        ('hold', 'Hold'),
        ('review', 'Review'),
        ('confirm', 'Confirm'),
        ('cancel', 'Cancel'),
    ]
    status = models.CharField(max_length=64, choices=choices)

    class Meta:
        permissions = (
            ('create_task', 'Create task'),
            ('update_task', 'Update task'),
        )

    def __str__(self) -> str:
        return self.name
