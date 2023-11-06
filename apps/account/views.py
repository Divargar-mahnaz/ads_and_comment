from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token

from apps.account.exceptions import LoginFail
from apps.account.models import User
from apps.account.serializer.account import LoginSerializer, RegisterSerializer
from common.base_view import NoAuthAPIView
from common.messages import USER_CREATED_SUCCESSFULLY
from common.response import Response


class RegisterAPIView(NoAuthAPIView):
    @swagger_auto_schema(
        request_body=RegisterSerializer())
    def post(self, request):
        print(request.data)
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.data)
        return Response({'message': USER_CREATED_SUCCESSFULLY}, status=status.HTTP_201_CREATED)


class LoginAPIView(NoAuthAPIView):
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        request_body=LoginSerializer())
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user is None:
            raise LoginFail
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
