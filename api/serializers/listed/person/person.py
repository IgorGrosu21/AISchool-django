from ..user import UserSerializer

from ..._helpers import RelatedSerializer, RetrieveableSerializer

class PersonSerializer(RelatedSerializer, RetrieveableSerializer):
  user = UserSerializer()

  class Meta:
    nested_fields = {
      'one': {
        'user': 'mutate'
      }
    }