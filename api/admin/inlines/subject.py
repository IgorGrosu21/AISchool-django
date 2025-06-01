from django.contrib import admin

from api.models import Subject

class SubjectInline(admin.TabularInline):
  model = Subject
  extra = 0