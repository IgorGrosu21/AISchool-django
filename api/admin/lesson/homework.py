from django.contrib import admin

from api.models import Homework

from ..inlines import HomeworkPhotoInline

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
  inlines = [HomeworkPhotoInline]