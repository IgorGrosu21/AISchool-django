from ..user import DetailedUserSerializer

from ..._helpers import EditableSerializer

class DetailedPersonSerializer(EditableSerializer):
  user = DetailedUserSerializer()