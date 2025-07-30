from django.contrib import admin

from api.models import manual as models
  
from .inlines import ModuleInline, TopicInline, TaskInline, TheoryInline

@admin.register(models.Balance)
class BalanceAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Manual)
class ManualAdmin(admin.ModelAdmin):
  list_filter = ['subject', 'grade']
  inlines = [ModuleInline]

@admin.register(models.Module)
class ModuleAdmin(admin.ModelAdmin):
  inlines = [TopicInline]
  
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Theory)
class TheoryAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
  inlines = [TaskInline, TheoryInline]