from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.posting.models import Advertising
from apps.posting.serializers import CommentSerializer, AdvertisingSerializer, AdvertisingSwaggerSerializer, \
    CommentSwaggerSerializer, AdvertisingListSerializer
from common.base_view import RetrieveUpdateDestroyView


class CommentCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if getattr(self, 'swagger_fake_view', False):
            return CommentSwaggerSerializer
        return CommentSerializer

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        return self.create(request, *args, **kwargs)


class AdvertisingCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Advertising.objects.all()

    def get_serializer_class(self):
        if getattr(self, 'swagger_fake_view', False):
            return AdvertisingSwaggerSerializer
        if self.request.method == 'GET':
            return AdvertisingListSerializer
        else:
            return AdvertisingSerializer


class AdvertisingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyView):
    queryset = Advertising.objects.all()

    def get_serializer_class(self):
        if getattr(self, 'swagger_fake_view', False):
            return AdvertisingSwaggerSerializer
        return AdvertisingSerializer
