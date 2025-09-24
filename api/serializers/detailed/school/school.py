from ..can_edit import CanEditSerializer
from ...media import DetailedMediaSerializer
from ...name import KlassNameSerializer, KlassNameWithGroupsSerializer, SchoolNameWithTimeTableSerializer, SubjectNameSerializer
from ...listed import PositionSerializer, SchoolSerializer, LessonTimeSerializer

from ..._helpers import RelatedSerializer

class DetailedSchoolSerializer(SchoolSerializer, RelatedSerializer, CanEditSerializer):
  staff = PositionSerializer(many=True)
  files = DetailedMediaSerializer(many=True, read_only=True)

  class Meta(SchoolSerializer.Meta):
    fields = SchoolSerializer.Meta.fields + ['can_edit', 'desc', 'phones', 'emails', 'work_hours', 'staff', 'files']
    nested_fields = {
      'many': {
        'staff': 'mutate',
      },
    }

class SchoolWithKlassesSerializer(RelatedSerializer, CanEditSerializer):
  klasses = KlassNameSerializer(many=True)

  class Meta(SchoolSerializer.Meta):
    fields = ['id', 'name', 'can_edit', 'klasses', 'slug']
    nested_fields = {
      'many': {
        'klasses': 'mutate'
      },
    }

class SchoolWithTimetableSerializer(RelatedSerializer, SchoolNameWithTimeTableSerializer, CanEditSerializer):
  klasses = KlassNameWithGroupsSerializer(many=True)
  timetable = LessonTimeSerializer(many=True)
  subjects = SubjectNameSerializer(many=True)

  class Meta(SchoolNameWithTimeTableSerializer.Meta):
    fields = ['id', 'name', 'can_edit', 'klasses', 'staff', 'timetable', 'subjects', 'slug']
    nested_fields = {
      'many': {
        'klasses': 'mutate',
        'timetable': 'mutate',
        'subjects': 'retrieve'
      },
    }