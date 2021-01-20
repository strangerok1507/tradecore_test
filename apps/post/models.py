from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    text = models.TextField(_('text'))
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'post: {self.post_id}, user: {self.user_id}'
