from django.contrib import admin

from api.models import Social

class SocialInline(admin.TabularInline):
  model = Social
  extra = 0