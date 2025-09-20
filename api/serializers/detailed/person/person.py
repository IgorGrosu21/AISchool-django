from ..can_edit import CanEditSerializer
from ..user import DetailedUserSerializer

from ..._helpers import RelatedSerializer

class DetailedPersonSerializer(RelatedSerializer, CanEditSerializer):
  user = DetailedUserSerializer()