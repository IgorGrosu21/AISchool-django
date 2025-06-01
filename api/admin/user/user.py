from django.contrib import admin

from api.models import User

from ..inlines import SocialInline

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  inlines = [SocialInline]