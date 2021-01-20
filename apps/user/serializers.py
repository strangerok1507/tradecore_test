from rest_framework.serializers import ModelSerializer

from apps.post.serializers import PostSerializer
from apps.user.models import User


class UserSerializer(ModelSerializer):
    posts_by_user = PostSerializer(
        source='post_set', many=True, read_only=True
    )

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'get_full_name', 'is_active',
            'posts_by_user', 'email', 'is_staff', 'date_joined', 'last_login',
        )
        read_only_fields = (
            'last_login', 'date_joined', 'is_staff', 'id', 'is_staff',
            'posts_by_user'
        )

    def get_quantity_of_post(self, instance):
        return instance.post_set.count()


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'password'
        )
        read_only_fields = ('id',)
