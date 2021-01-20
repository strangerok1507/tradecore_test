from rest_framework import status
from rest_framework.permissions import IsAuthenticated, NOT
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.user.models import User
from apps.user.serializers import CreateUserSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-id')

    def get_permissions(self):
        if self.action == 'create':
            return [NOT(IsAuthenticated()), ]
        else:
            return super(UserViewSet, self).get_permissions()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        else:
            return super(UserViewSet, self).get_serializer_class()

    def perform_create(self, serializer):
        return User.objects.create_user(**serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        serializer = self.serializer_class(instance=instance)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
