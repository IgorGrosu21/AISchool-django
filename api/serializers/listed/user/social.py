from rest_framework.serializers import ModelSerializer

from api.models import Social

class SocialSerializer(ModelSerializer):
  class Meta:
    fields = ['type', 'link']
    model = Social