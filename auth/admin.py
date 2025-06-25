from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AuthUserCreationForm, AuthUserChangeForm
from .models import AuthUser

class AuthUserAdmin(UserAdmin):
  add_form = AuthUserCreationForm
  form = AuthUserChangeForm
  model = AuthUser
  list_display = ('email', 'is_staff', 'is_verified')
  list_filter = ('email', 'is_staff', 'is_verified',)
  fieldsets = (
    (None, {'fields': ('email', 'password', 'is_verified')}),
    ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
  )
  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': (
        'email', 'password1', 'password2', 'is_staff',
        'is_active', 'groups', 'user_permissions'
      )}
    ),
  )
  search_fields = ('email',)
  ordering = ('email',)


admin.site.register(AuthUser, AuthUserAdmin)