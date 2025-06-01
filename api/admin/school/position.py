from django.contrib import admin

from api.models import Position

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
  pass