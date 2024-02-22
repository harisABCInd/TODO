from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL, related_name='group')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self) -> str:
        return self.email
    

class Task(models.Model):
    name = models.CharField(max_length=128, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_by')
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_to')
    choices = [
        ('in_progress', 'In progress'),
        ('complete', 'Complete'),
        ('hold', 'Hold'),
        ('review', 'Review'),
        ('confirm', 'Confirm'),
        ('cancel', 'Cancel'),
    ]
    status = models.CharField(max_length=64, choices=choices)

    def __str__(self) -> str:
        return self.name
