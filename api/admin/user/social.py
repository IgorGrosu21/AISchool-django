from django.contrib import admin

from api.models import Social

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
  pass