from django.contrib import admin

from api.models import Topic

from ..inlines import TaskInline, TheoryInline

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
  inlines = [TaskInline, TheoryInline]