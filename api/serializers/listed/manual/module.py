from rest_framework.serializers import ModelSerializer

from api.models import Module

from .topic import TopicSerializer
from .manual import ManualSerializer
from .balance import BalanceSerializer

class ModuleWithManualSerializer(ModelSerializer):
  subject = ManualSerializer()
  
  class Meta:
    fields = ['name', 'subject', 'slug']
    model = Module
  

class ModuleSerializer(ModuleWithManualSerializer):
  subject = None
  topics = TopicSerializer(many=True)
  balance = BalanceSerializer()
  
  class Meta(ModuleWithManualSerializer.Meta):
    fields = ['name', 'topics', 'balance', 'slug']