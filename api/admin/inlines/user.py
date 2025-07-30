from django.contrib import admin

from api.models import user as models

class SocialInline(admin.TabularInline):
  model = models.Social
  extra = 0