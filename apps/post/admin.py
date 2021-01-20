from django.contrib import admin

from apps.post.models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    empty_value_display = 'unknown'
    list_display = ('title', 'user',)
    list_display_links = ('title', 'user',)
    ordering = ('id',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    empty_value_display = 'unknown'
    list_display = ('post', 'user',)
    list_display_links = ('post', 'user',)
    ordering = ('id',)
