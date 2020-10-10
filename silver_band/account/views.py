from rest_framework import generics, status
from .serializers import CreateUserSerializer, LoginUserSerializer, UserSerializer
from rest_framework.response import Response

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

        return Response({"user": UserSerializer(user).data})


class LoginView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.validated_data

        return Response({"user": UserSerializer(user).data, "token": token})
