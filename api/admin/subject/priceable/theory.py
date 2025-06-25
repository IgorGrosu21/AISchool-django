from django.contrib import admin

from api.models import Theory

@admin.register(Theory)
class TheoryAdmin(admin.ModelAdmin):
  pass