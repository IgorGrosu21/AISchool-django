from django.contrib import admin

from api.models import SubjectName

@admin.register(SubjectName)
class SubjectNameAdmin(admin.ModelAdmin):
  list_filter = ['type__country', 'type__name', 'lang']