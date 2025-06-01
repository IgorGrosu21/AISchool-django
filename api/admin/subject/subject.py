from django.contrib import admin

from api.models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
  list_filter = ['name', 'grade']