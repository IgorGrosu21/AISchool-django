from django.contrib import admin

from api.models import Student

class StudentInline(admin.TabularInline):
  model = Student
  extra = 0