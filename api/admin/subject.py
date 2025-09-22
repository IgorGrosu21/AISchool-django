from django.contrib import admin

from api.models import SubjectModels as models

from .inlines import SubjectInline, ManualInline

@admin.register(models.SubjectType)
class SubjectTypeAdmin(admin.ModelAdmin):
  list_filter = ['country', 'name']
  inlines = [SubjectInline]
  
@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
  list_filter = ['type__country', 'type__name', 'lang']
  inlines = [ManualInline]