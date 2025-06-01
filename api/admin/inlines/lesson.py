from django.contrib import admin

from api.models import HomeworkPhoto, Homework, Lesson, Note, SpecificLessonPhoto

class HomeworkPhotoInline(admin.TabularInline):
  model = HomeworkPhoto
  extra = 0

class HomeworkInline(admin.TabularInline):
  model = Homework
  extra = 0
  
class LessonInline(admin.TabularInline):
  model = Lesson
  extra = 0
  
class NoteInline(admin.TabularInline):
  model = Note
  extra = 0

class SpecificLessonPhotoInline(admin.TabularInline):
  model = SpecificLessonPhoto
  extra = 0