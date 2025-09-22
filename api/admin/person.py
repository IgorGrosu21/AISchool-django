from django.contrib import admin

from api.models import PersonModels as models

from .inlines import (
  ParentStudentInline, 
  HomeworkInline, NoteInline, StudentGroupInline,
  TeacherSubjectInline, LessonInline, PositionInline, GroupInline)

@admin.register(models.Parent)
class ParentAdmin(admin.ModelAdmin):
  inlines = [ParentStudentInline]

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
  inlines = [ParentStudentInline, StudentGroupInline, HomeworkInline, NoteInline]

@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
  inlines = [TeacherSubjectInline, PositionInline, GroupInline, LessonInline]