from django.contrib import admin

from api.models import Region, City

class RegionInline(admin.TabularInline):
  model = Region
  extra = 0
  
class CityInline(admin.TabularInline):
  model = City
  extra = 0