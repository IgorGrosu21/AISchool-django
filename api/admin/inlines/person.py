from django.contrib import admin

from api.models import person as models

class StudentInline(admin.TabularInline):
  model = models.Student
  extra = 0