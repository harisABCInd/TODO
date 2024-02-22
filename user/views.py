from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from core.models import User
from user.permissions import IsAdminOnly
from user.serializers import GroupSerializer, UserSerializer, UserDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import Group
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
# Create your views here.


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOnly]


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOnly]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'list':
            return UserSerializer
        
        return self.serializer_class
