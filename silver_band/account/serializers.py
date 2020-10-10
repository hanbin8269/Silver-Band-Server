from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_jwt import utils
from django.utils.translation import ugettext as _
import jwt


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        credentials = {"email": data["email"], "password": data["password"]}
        user = authenticate(**credentials)

        if user and user.is_active:
            payload = {"id": user.id, "email": user.email, "username": user.username}

            token = utils.jwt_encode_handler(payload)

            return (user, token)

        msg = _("Unable to login with provided credentials")
        raise serializers.ValidationError(msg)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")