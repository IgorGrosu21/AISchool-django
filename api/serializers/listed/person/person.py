from ..user import UserSerializer

from ..._helpers import RelatedSerializer

class PersonSerializer(RelatedSerializer):
  user = UserSerializer()
  
  class Meta:
    nested_fields = {
      'one': {
        'user': 'mutate'
      }
    }