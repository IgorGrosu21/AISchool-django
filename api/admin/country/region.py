from django.contrib import admin

from api.models import Region

from ..inlines import CityInline

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
  inlines = [CityInline]