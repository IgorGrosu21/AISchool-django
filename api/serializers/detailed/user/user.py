from ..can_edit import CanEditSerializer
from ...listed import SocialSerializer, CitySerializer, UserSerializer

from ..._helpers import RelatedSerializer

class DetailedUserSerializer(UserSerializer, RelatedSerializer, CanEditSerializer):
  socials = SocialSerializer(many=True)
  city = CitySerializer()

  class Meta(UserSerializer.Meta):
    fields = UserSerializer.Meta.fields + ['socials', 'city', 'lang', 'can_edit']
    nested_fields = {
      'one': {
        'city': 'retrieve'
      },
      'many': {
        'socials': 'mutate'
      }
    }

class UserRoutesSerializer(UserSerializer):
  class Meta(UserSerializer.Meta):
    fields = UserSerializer.Meta.fields + ['is_account_verified', 'klass_link', 'school_link', 'diary_link', 'journal_link']