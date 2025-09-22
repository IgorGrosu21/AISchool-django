from django.contrib import admin

from api.models import SchoolModels as models

class GroupInline(admin.TabularInline):
  model = models.Group
  extra = 0

class KlassInline(admin.TabularInline):
  model = models.Klass
  extra = 0

class SchoolPhotoInline(admin.TabularInline):
  model = models.SchoolPhoto
  extra = 0
  
class PositionInline(admin.TabularInline):
  model = models.Position
  extra = 0