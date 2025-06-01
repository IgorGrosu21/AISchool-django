from django.contrib import admin

from api.models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
  pass