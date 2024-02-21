from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from user.serializers import GroupSerializer
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
    permission_classes = [IsAuthenticated]