from django.contrib import admin

from api.models import Klass

from ..inlines import StudentInline, LessonInline

@admin.register(Klass)
class KlassAdmin(admin.ModelAdmin):
  inlines = [StudentInline, LessonInline]