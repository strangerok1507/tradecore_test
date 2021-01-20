from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from apps.user.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    empty_value_display = 'unknown'
    list_display = ('email', 'is_staff',)
    list_display_links = ('email',)
    list_filter = ('is_staff',)
    search_fields = ('first_name', 'last_name', 'email',)
    fieldsets = (
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'email',)
        }),
        (_('Permissions'), {
            'fields': ('is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    ordering = ('id',)
