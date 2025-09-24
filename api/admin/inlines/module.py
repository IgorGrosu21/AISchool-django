from django.contrib import admin

from api.models import ManualModels as models

class ModuleInline(admin.TabularInline):
  model = models.Module
  extra = 0

class TopicInline(admin.TabularInline):
  model = models.Topic
  extra = 0

class TaskInline(admin.TabularInline):
  model = models.Task
  extra = 0

class TheoryInline(admin.TabularInline):
  model = models.Theory
  extra = 0