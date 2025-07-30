from api.models import Social

from ..._helpers import CreatableSerializer

class SocialSerializer(CreatableSerializer):
  class Meta:
    fields = ['id', 'type', 'link', 'user']
    model = Social