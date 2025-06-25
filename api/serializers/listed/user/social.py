from rest_framework.serializers import CharField

from api.models import Social, User

from ..._helpers import EditableSerializer

class SocialSerializer(EditableSerializer):
  id = CharField(allow_blank=True, required=False)
  
  class Meta:
    fields = ['id', 'type', 'link', 'user']
    model = Social