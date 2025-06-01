from django.contrib import admin

from api.models import Klass, SchoolPhoto, Position

class KlassInline(admin.TabularInline):
  model = Klass
  extra = 0

class SchoolPhotoInline(admin.TabularInline):
  model = SchoolPhoto
  extra = 0
  
class PositionInline(admin.TabularInline):
  model = Position
  extra = 0