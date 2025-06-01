from django.contrib import admin

from api.models import SpecificLesson

from ..inlines import SpecificLessonPhotoInline, NoteInline, HomeworkInline

@admin.register(SpecificLesson)
class SpecificLessonAdmin(admin.ModelAdmin):
  inlines = [SpecificLessonPhotoInline, NoteInline, HomeworkInline]