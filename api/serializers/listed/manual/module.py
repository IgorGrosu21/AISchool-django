from rest_framework.serializers import ModelSerializer

from api.models import Module

from .topic import TopicSerializer
from .manual import ManualSerializer
from .balance import BalanceSerializer

class ModuleWithManualSerializer(ModelSerializer):
  manual = ManualSerializer()

  class Meta:
    fields = ['name', 'manual', 'slug']
    model = Module


class ModuleSerializer(ModuleWithManualSerializer):
  manual = None
  topics = TopicSerializer(many=True)
  balance = BalanceSerializer()

  class Meta(ModuleWithManualSerializer.Meta):
    fields = ['name', 'topics', 'balance', 'slug']