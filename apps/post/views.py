from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from apps.post.models import Like, Post
from apps.post.serializers import LikeSerializer, PostSerializer


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-id')

    def get_queryset(self):
        if self.action in ['retrieve', 'list', ]:
            return self.queryset
        else:
            return self.queryset.filter(user=self.request.user)


class LikeViewSet(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def get_queryset(self):
        if self.action == ['destroy']:
            return self.queryset.filter(user=self.request.user)
        else:
            return self.queryset
