from django.contrib import admin

from api.models import Teacher

from ..inlines import PositionInline, LessonInline

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
  inlines = [PositionInline, LessonInline]