from ..can_edit import CanEditSerializer
from ...listed import StudentSerializer, LessonSerializer, TeacherSerializer, KlassSerializer
from ...name import SchoolNameWithTimeTableSerializer

from ..._helpers import RelatedSerializer
    
class DetailedKlassSerializer(KlassSerializer, RelatedSerializer, CanEditSerializer):
  students = StudentSerializer(many=True)
  lessons = LessonSerializer(many=True)
  teacher = TeacherSerializer(required=False, allow_null=True)
  school = SchoolNameWithTimeTableSerializer(read_only=True)
  
  class Meta(KlassSerializer.Meta):
    fields = KlassSerializer.Meta.fields + ['can_edit', 'teacher', 'students', 'lessons']
    nested_fields = {
      'one': {
        'teacher': 'retrieve'
      },
      'many': {
        'students': 'mutate',
        'lessons': 'mutate'
      },
    }