from django.contrib import admin

from api.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  pass