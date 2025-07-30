from rest_framework.serializers import ModelSerializer

from api.models import Balance

class BalanceSerializer(ModelSerializer):
  class Meta:
    exclude = ['id', 'networth']
    model = Balance