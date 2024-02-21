from rest_framework import serializers
from core.models import User
from django.contrib.auth.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
        read_only_fields = ('id', )


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=64, write_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'group', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5},
        }
        read_only_fields = ('id', )
    
    def create(self, validated_data):
        # Remove confirm_password from validated_data
        confirm_password = validated_data.pop('confirm_password')

        # Check if passwords match
        if validated_data['password'] != confirm_password:
            raise serializers.ValidationError("Passwords do not match")

        # Create and return the user
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

class UserDetailSerializer(UserSerializer):
    group = GroupSerializer()
    