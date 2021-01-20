import factory

from apps.post.models import Like, Post
from apps.user.tests.factories import UserFactory


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence')
    text = factory.Faker('text')
    user = factory.SubFactory(UserFactory)


class LikeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Like

    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
