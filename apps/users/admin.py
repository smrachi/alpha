from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from apps.users.models import CustomUser

from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    ordering = ['pkid']
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['pkid', 'id', 'username', 'email',
                    'first_name', 'last_name', 'is_staff', 'is_active']
    list_display_links = ['pkid', 'id', 'username']
    list_filter = ['is_staff', 'is_active', 'is_superuser']
    fieldsets = (
        (_('Login Credentials'), {'fields': ('username', 'password',)}),
        (_('Personal Information'), {
         'fields': ('email', 'first_name', 'last_name',)}),
        (_('Permissions and Groups'), {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    readonly_fields = ['last_login', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']


admin.site.register(CustomUser, CustomUserAdmin)
