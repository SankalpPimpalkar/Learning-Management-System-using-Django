from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

@admin.register(Account)
class AccountAdmin(UserAdmin):
    model = Account
    list_display = ('email', 'name', 'role', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone', 'role', 'avatar')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone', 'password1', 'password2', 'role', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)
