from rest_framework.serializers import ModelSerializer

from api.models import Topic
from .balance import BalanceSerializer

class TopicSerializer(ModelSerializer):
  balance = BalanceSerializer()
  
  class Meta:
    fields = ['name', 'balance', 'slug']
    model = Topic