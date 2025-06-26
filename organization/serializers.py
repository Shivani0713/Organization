from .models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

#----------------- SignUp with unique EMail ------------#
class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_check = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password", "password_check"]

    def validate(self, data):
        if data['password'] != data['password_check']:
            raise serializers.ValidationError("Both Passwords should be the same!")
        return data

    def create(self, validated_data):
        validated_data.pop('password_check')
        return User.objects.create_user(**validated_data)

#------------ User serializers ------------#
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

#------------- Organization Serializer --------#
class OrganizationSerializer(serializers.ModelSerializer):
    admin = UserDisplaySerializer(read_only=True)

    class Meta:
        model = Organization
        fields = ["org_name", "admin"]

#---------------- Member Serializer -----------#
class MemberSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = Member
        fields = ["organization", "user"]
