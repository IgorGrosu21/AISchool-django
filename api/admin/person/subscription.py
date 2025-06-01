from django.contrib import admin

from api.models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
  pass