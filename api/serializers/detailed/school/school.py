from api.models import School

from ..can_edit import CanEditSerializer
from ...media import DetailedMediaSerializer
from ...name import KlassNameSerializer, SchoolNameWithTimeTableSerializer
from ...listed import PositionSerializer, SchoolSerializer, LessonTimeSerializer

from ..._helpers import EditableSerializer

class DetailedSchoolSerializer(SchoolSerializer, EditableSerializer, CanEditSerializer):
  staff = PositionSerializer(many=True)
  photos = DetailedMediaSerializer(many=True, read_only=True)
  
  class Meta(SchoolSerializer.Meta):
    fields = SchoolSerializer.Meta.fields + ['can_edit', 'desc', 'phones', 'emails', 'work_hours', 'staff', 'klasses', 'photos']
    nested_fields = {
      'many': {
        'staff': 'mutate',
      },
    }
    
class SchoolWithKlassesSerializer(EditableSerializer, CanEditSerializer):
  klasses = KlassNameSerializer(many=True)
  
  class Meta(SchoolSerializer.Meta):
    fields = ['id', 'name', 'can_edit', 'klasses']
    nested_fields = {
      'many': {
        'klasses': 'mutate'
      },
    }
    
class SchoolWithTimetableSerializer(EditableSerializer, SchoolNameWithTimeTableSerializer, CanEditSerializer):
  klasses = KlassNameSerializer(many=True, read_only=True)
  timetable = LessonTimeSerializer(many=True)
  
  class Meta(SchoolSerializer.Meta):
    fields = ['id', 'name', 'can_edit', 'klasses', 'staff', 'timetable']
    nested_fields = {
      'many': {
        'timetable': 'mutate'
      },
    }