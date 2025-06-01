from rest_framework.serializers import ModelSerializer

from api.models import Subscription

class SubscriptionSerializer(ModelSerializer):
  class Meta:
    exclude = ['id']
    model = Subscription