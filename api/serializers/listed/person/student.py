from rest_framework.serializers import IntegerField

from api.models import Student

from .person import PersonSerializer
from .balance import BalanceSerializer
from .subscription import SubscriptionSerializer

class StudentSerializer(PersonSerializer):
  balance = BalanceSerializer(read_only=True)
  subscription = SubscriptionSerializer(read_only=True)
  rank = IntegerField()
  
  class Meta:
    fields = ['id', 'user', 'balance', 'subscription', 'rank', 'is_manager']
    model = Student