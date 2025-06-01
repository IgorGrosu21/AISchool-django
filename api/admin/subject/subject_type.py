from django.contrib import admin

from api.models import SubjectType

@admin.register(SubjectType)
class SubjectTypeAdmin(admin.ModelAdmin):
  list_filter = ['country', 'name']