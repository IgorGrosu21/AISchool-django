from django.contrib import admin

from api.models import CountryModels as models

from .inlines import CityInline, RegionInline

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
  inlines = [RegionInline]

@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
  inlines = [CityInline]