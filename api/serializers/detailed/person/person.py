from rest_framework.serializers import Serializer, UUIDField, CharField


from ..can_edit import CanEditSerializer
from ..user import DetailedUserSerializer
from ...listed import UserSerializer

from ..._helpers import RelatedSerializer

class DetailedPersonSerializer(RelatedSerializer, CanEditSerializer):
  user = DetailedUserSerializer()

class PersonHomeSerializer(Serializer):
  id = UUIDField(read_only=True)
  user = UserSerializer(read_only=True)
  profile_type = CharField(read_only=True)