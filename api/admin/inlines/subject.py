from django.contrib import admin

from api.models import subject as models

class SubjectInline(admin.TabularInline):
  model = models.Subject
  extra = 0