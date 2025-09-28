from django.db.models import Model
from rest_framework.serializers import ModelSerializer

from api.models import Module

from .topic import TopicSerializer
from .manual import ManualSerializer
from .balance import BalanceSerializer

class ModuleWithManualSerializer(ModelSerializer):
  manual = ManualSerializer()

  class Meta:
    fields = ['name', 'manual', 'slug', 'start_page', 'end_page']
    model = Module

class ModuleSerializer(ModelSerializer):
  topics = TopicSerializer(many=True)
  balance = BalanceSerializer()

  class Meta:
    fields = ['name', 'topics', 'balance', 'slug', 'start_page', 'end_page']
    model = Module