from rest_framework import serializers

from common.messages import ON_COMMENT_IS_ALLOWED
from .models import Comment, Advertising
from django.core.exceptions import NON_FIELD_ERRORS

from ..account.serializer.account import UserInfoSerializer


class CommentSwaggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['advertising', 'content']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['advertising', 'content', 'user']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Comment.objects.all(),
                fields=('advertising', 'user'),
                message=ON_COMMENT_IS_ALLOWED
            )
        ]

    def is_valid(self, *args, **kwargs):
        self.initial_data['user'] = self.context['request'].user.pk
        return super(CommentSerializer, self).is_valid(*args, **kwargs)


class AdvertisingSwaggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = ['content']


class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = ['content', 'user']

    def is_valid(self, *args, **kwargs):
        self.initial_data['user'] = self.context['request'].user.pk
        return super(AdvertisingSerializer, self).is_valid(*args, **kwargs)


class AdvertisingListSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source='comment_set', many=True)
    user = UserInfoSerializer()

    class Meta:
        model = Advertising
        fields = ['id', 'user', 'comments', 'content']
