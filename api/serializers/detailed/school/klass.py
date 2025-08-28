from ..can_edit import CanEditSerializer
from ...listed import StudentSerializer, TeacherSerializer, KlassSerializer
from ...name import SchoolNameWithTimeTableSerializer, LessonNameSerializer, GroupNameSerializer

from ..._helpers import RelatedSerializer
    
class DetailedKlassSerializer(KlassSerializer, RelatedSerializer, CanEditSerializer):
  students = StudentSerializer(many=True)
  lessons = LessonNameSerializer(many=True)
  groups = GroupNameSerializer(many=True)
  teacher = TeacherSerializer(required=False, allow_null=True)
  school = SchoolNameWithTimeTableSerializer(read_only=True)
  
  class Meta(KlassSerializer.Meta):
    fields = KlassSerializer.Meta.fields + ['can_edit', 'teacher', 'students', 'lessons', 'groups']
    nested_fields = {
      'one': {
        'teacher': 'mutate'
      },
      'many': {
        'students': 'mutate',
        'lessons': 'mutate',
        'groups': 'mutate'
      },
    }