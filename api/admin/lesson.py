from django.contrib import admin

from api.models import LessonModels as models

from .inlines import HomeworkPhotoInline, LessonInline, SpecificLessonInline, SpecificLessonPhotoInline, NoteInline, HomeworkInline

@admin.register(models.Homework)
class HomeworkAdmin(admin.ModelAdmin):
  inlines = [HomeworkPhotoInline]

@admin.register(models.LessonTime)
class LessonTimeAdmin(admin.ModelAdmin):
  inlines = [LessonInline]

@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
  inlines = [SpecificLessonInline]

@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
  pass

@admin.register(models.SpecificLesson)
class SpecificLessonAdmin(admin.ModelAdmin):
  inlines = [SpecificLessonPhotoInline, NoteInline, HomeworkInline]