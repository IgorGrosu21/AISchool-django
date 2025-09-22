from django.contrib import admin

from api.models import UserModels as models

from .inlines import SocialInline

@admin.register(models.Social)
class SocialAdmin(admin.ModelAdmin):
  pass

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
  inlines = [SocialInline]