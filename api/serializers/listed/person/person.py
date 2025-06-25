from rest_framework.serializers import UUIDField

from ..user import UserSerializer

from ..._helpers import EditableSerializer

class PersonSerializer(EditableSerializer):
  id = UUIDField()
  user = UserSerializer()
  
  class Meta:
    nested_fields = {
      'one': {
        'user': 'mutate'
      }
    }