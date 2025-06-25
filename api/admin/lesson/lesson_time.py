from django.contrib import admin

from api.models import LessonTime

@admin.register(LessonTime)
class LessonTimeAdmin(admin.ModelAdmin):
  pass