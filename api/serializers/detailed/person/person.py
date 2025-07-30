from ..user import DetailedUserSerializer

from ..._helpers import RelatedSerializer

class DetailedPersonSerializer(RelatedSerializer):
  user = DetailedUserSerializer()