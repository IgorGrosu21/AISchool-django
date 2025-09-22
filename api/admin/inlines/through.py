from django.contrib import admin

from api.models import PersonModels as models

class ParentStudentInline(admin.TabularInline):
  model = models.Parent.students.through

class StudentGroupInline(admin.TabularInline):
  model = models.Student.groups.through

class TeacherSubjectInline(admin.TabularInline):
  model = models.Teacher.subjects.through