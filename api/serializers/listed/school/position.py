from api.models import Position

from ..person import TeacherSerializer
from ...name import SchoolNameSerializer, PositionNameSerializer

from ..._helpers import RelatedSerializer, CreatableSerializer

class PositionSerializer(PositionNameSerializer, RelatedSerializer, CreatableSerializer):
  teacher = TeacherSerializer()
  school = SchoolNameSerializer()
  
  class Meta(PositionNameSerializer.Meta):
    fields = PositionNameSerializer.Meta.fields + ['id', 'school', 'type', 'is_manager']
    model = Position
    nested_fields = {
      'one': {
        'teacher': 'mutate',
        'school': 'retrieve'
      },
      'many': {
        'subject_names': 'retrieve'
      }
    }