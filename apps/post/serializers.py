from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from apps.post.models import Like, Post


class PostSerializer(serializers.ModelSerializer):
    quantity_of_like = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'text', 'user', 'quantity_of_like',
        )

    def get_quantity_of_like(self, instance):
        return instance.like_set.count()


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Like
        fields = ('id', 'post', 'user')

    def validate_post(self, instance):
        user = self.context['request'].user
        if instance.user == user:
            raise ValidationError(_('Users cannot like their own posts'))
        if Like.objects.filter(user=user, post=instance).exists():
            raise ValidationError(_('User already liked this post'))
        return instance
