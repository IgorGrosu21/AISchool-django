from django.contrib import admin

from api.models import LessonModels as models

class HomeworkPhotoInline(admin.TabularInline):
  model = models.HomeworkPhoto
  extra = 0

class HomeworkInline(admin.TabularInline):
  model = models.Homework
  extra = 0
  
class LessonInline(admin.TabularInline):
  model = models.Lesson
  extra = 0
  
class NoteInline(admin.TabularInline):
  model = models.Note
  extra = 0

class SpecificLessonPhotoInline(admin.TabularInline):
  model = models.SpecificLessonPhoto
  extra = 0

class SpecificLessonInline(admin.TabularInline):
  model = models.SpecificLesson
  extra = 0