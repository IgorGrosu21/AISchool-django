from rest_framework.serializers import ModelSerializer

from api.models import Module

from .topic import TopicSerializer
from .subject import SubjectSerializer
from .balance import BalanceSerializer

class ModuleWithSubjectSerializer(ModelSerializer):
  subject = SubjectSerializer()
  
  class Meta:
    fields = ['name', 'subject', 'slug']
    model = Module
  

class ModuleSerializer(ModuleWithSubjectSerializer):
  subject = None
  topics = TopicSerializer(many=True)
  balance = BalanceSerializer()
  
  class Meta(ModuleWithSubjectSerializer.Meta):
    fields = ['name', 'topics', 'balance', 'slug']