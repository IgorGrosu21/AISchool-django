from django.contrib import admin

from api.models import Module

from ..inlines import TopicInline

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
  inlines = [TopicInline]