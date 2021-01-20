from django.test import TestCase

from apps.user.tests.factories import UserFactory
from apps.user.serializers import UserSerializer


class TestUserSerializer(TestCase):

    def test_get_valid_user_fields(self):
        user = UserFactory()
        serializer = UserSerializer(user)
        self.assertEqual(serializer.data.get('email'), user.email)
        self.assertEqual(serializer.data.get('id'), user.id)
        self.assertIsNone(serializer.data.get('password'))
