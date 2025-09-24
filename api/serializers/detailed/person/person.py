from rest_framework.serializers import ModelSerializer


from ..can_edit import CanEditSerializer
from ..user import DetailedUserSerializer
from ...listed import UserSerializer

from ..._helpers import RelatedSerializer

class DetailedPersonSerializer(RelatedSerializer, CanEditSerializer):
  user = DetailedUserSerializer()

class PersonHomeSerializer(ModelSerializer):
  user = UserSerializer(read_only=True)

  class Meta:
    fields = ['id', 'user', 'profile_type']