from django.contrib import admin

from api.models import ModuleProgress

@admin.register(ModuleProgress)
class ModuleProgressAdmin(admin.ModelAdmin):
  pass