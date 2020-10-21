from rest_framework import generics, status
from rest_framework import viewsets
from .serializers import (
    CreateUserSerializer,
    LoginUserSerializer,
    UserSerializer,
    WearerSerializer,
)
from rest_framework.response import Response
from .models import Wearer, User

# Create your views here.


class RegistrationView(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["password"]) < 6:
            message = {"message": "password is too short"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {"user": UserSerializer(user).data}, status=status.HTTP_201_CREATED
        )


class LoginView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.validated_data
        return Response(
            {"user": UserSerializer(user).data, "token": token},
            status=status.HTTP_200_OK,
        )


class WearerViewSet(generics.GenericAPIView):
    serializer_class = WearerSerializer

    def get(self, request, *args, **kwargs):
        wearer_data = Wearer.objects.get(id=kwargs["user_id"])
        return Response(
            {"wearer": self.get_serializer(data=weared_data).data},
            status=status.HTTP_200_OK,
        )

    def post(self, request, *args, **kwargs):
        wearer_data = Wearer.objects.create(**request.data)
        # user_data get 들어가기 전에
        user_data = User.objects.get(id=kwargs["user_id"])

        serializer = self.get_serializer(data=wearer_data)
        serializer.is_valid()

        return Response({"wearer": serializer.data}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        pass
