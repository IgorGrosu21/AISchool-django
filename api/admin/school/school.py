from django.contrib import admin

from api.models import School

from ..inlines import KlassInline, PositionInline, SchoolPhotoInline

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
  inlines = [KlassInline, PositionInline, SchoolPhotoInline]