from django.contrib import admin

from api.models import user as models

from .inlines import SocialInline

@admin.register(models.Social)
class SocialAdmin(admin.ModelAdmin):
  pass

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
  inlines = [SocialInline]