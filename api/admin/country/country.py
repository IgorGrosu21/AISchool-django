from django.contrib import admin

from api.models import Country

from ..inlines import RegionInline

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
  inlines = [RegionInline]