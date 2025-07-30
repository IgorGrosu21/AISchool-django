from django.contrib import admin

from api.models import Parent, Student, Teacher

class ParentStudentInline(admin.TabularInline):
  model = Parent.students.through

class StudentGroupInline(admin.TabularInline):
  model = Student.groups.through

class TeacherSubjectInline(admin.TabularInline):
  model = Teacher.subjects.through