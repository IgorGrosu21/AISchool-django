from django.contrib import admin

from api.models import SchoolModels as models

from .inlines import (
  LessonInline, StudentGroupInline,
  StudentInline, GroupInline,
  KlassInline, PositionInline, SchoolPhotoInline
)

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
  inlines = [StudentGroupInline, LessonInline]

@admin.register(models.Klass)
class KlassAdmin(admin.ModelAdmin):
  inlines = [GroupInline, StudentInline, LessonInline]

@admin.register(models.Position)
class PositionAdmin(admin.ModelAdmin):
  pass

@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
  inlines = [KlassInline, PositionInline, SchoolPhotoInline]