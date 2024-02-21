from django.contrib import admin
from core.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'first_name', 'last_name', 'get_group_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'group')}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'group', 'password1', 'password2')
        }),
    )

    def get_group_name(self, obj):
        return obj.group.name if obj.group else None

    get_group_name.short_description = 'Group'

admin.site.register(User, UserAdmin)