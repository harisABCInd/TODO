from rest_framework import serializers
from core.models import User
from django.contrib.auth.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
        read_only_fields = ('id', )
