from django.contrib import admin

from api.models import country as models

class RegionInline(admin.TabularInline):
  model = models.Region
  extra = 0
  
class CityInline(admin.TabularInline):
  model = models.City
  extra = 0