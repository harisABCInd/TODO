from django.shortcuts import render
from rest_framework import viewsets
from user.serializers import GroupSerializer
from django.contrib.auth.models import Group
# Create your views here.


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()