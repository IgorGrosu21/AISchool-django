from django.contrib import admin

from api.models import Balance

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
  pass