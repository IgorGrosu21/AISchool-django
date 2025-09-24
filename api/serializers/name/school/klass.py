from api.models import Klass

from ..person import StudentNameSerializer
from .group import GroupNameSerializer

from ..._helpers import CreatableSerializer, RelatedSerializer

class KlassNameSerializer(CreatableSerializer, RelatedSerializer):
  class Meta:
    fields = ['id', 'grade', 'letter', 'profile', 'school', 'slug']
    model = Klass

class KlassNameWithGroupsSerializer(KlassNameSerializer):
  students = StudentNameSerializer(many=True, read_only=True)
  groups = GroupNameSerializer(many=True)

  class Meta(KlassNameSerializer.Meta):
    fields = KlassNameSerializer.Meta.fields + ['groups', 'students']
    nested_fields = {
      'many': {
        'groups': 'mutate'
      }
    }