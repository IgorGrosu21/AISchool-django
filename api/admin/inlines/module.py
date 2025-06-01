from django.contrib import admin

from api.models import Task, Theory, Topic, Module

class ModuleInline(admin.TabularInline):
  model = Module
  extra = 0

class TopicInline(admin.TabularInline):
  model = Topic
  extra = 0

class TaskInline(admin.TabularInline):
  model = Task
  extra = 0
  
class TheoryInline(admin.TabularInline):
  model = Theory
  extra = 0