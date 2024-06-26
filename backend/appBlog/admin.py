from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import myUser, Post, Comment
# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'date_joined')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(myUser, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
