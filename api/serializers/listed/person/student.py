from rest_framework.serializers import IntegerField

from .person import PersonSerializer
from ..manual import BalanceSerializer
from .subscription import SubscriptionSerializer
from ...name import StudentNameSerializer

class StudentSerializer(PersonSerializer, StudentNameSerializer):
  balance = BalanceSerializer(read_only=True)
  subscription = SubscriptionSerializer(read_only=True)
  rank = IntegerField(read_only=True)
  
  class Meta(PersonSerializer.Meta, StudentNameSerializer.Meta):
    fields = StudentNameSerializer.Meta.fields + ['balance', 'subscription', 'rank', 'is_manager']