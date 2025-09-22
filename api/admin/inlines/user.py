from django.contrib import admin

from api.models import UserModels as models

class SocialInline(admin.TabularInline):
  model = models.Social
  extra = 0