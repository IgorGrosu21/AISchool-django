from ..can_edit import CanEditSerializer
from ...listed import StudentSerializer, LessonSerializer, TeacherSerializer, KlassSerializer
from ...name import SchoolNameWithTimeTableSerializer

from ..._helpers import EditableSerializer
    
class DetailedKlassSerializer(KlassSerializer, EditableSerializer, CanEditSerializer):
  students = StudentSerializer(many=True)
  timetable = LessonSerializer(many=True)
  teacher = TeacherSerializer(required=False, allow_null=True)
  school = SchoolNameWithTimeTableSerializer(read_only=True)
  
  class Meta(KlassSerializer.Meta):
    fields = KlassSerializer.Meta.fields + ['can_edit', 'teacher', 'students', 'timetable']
    nested_fields = {
      'one': {
        'teacher': 'retrieve'
      },
      'many': {
        'students': 'mutate',
        'timetable': 'mutate'
      },
    }

class KlassWithDiarySerializer(KlassSerializer, EditableSerializer, CanEditSerializer):
  timetable = LessonSerializer(many=True, read_only=True)
  school = SchoolNameWithTimeTableSerializer(read_only=True)
  
  class Meta(KlassSerializer.Meta):
    fields = KlassSerializer.Meta.fields + ['can_edit', 'timetable']
    nested_fields = {}
    
class KlassWithStudentsSerializer(KlassSerializer):
  students = StudentSerializer(many=True, read_only=True)
  
  class Meta(KlassSerializer.Meta):
    fields = KlassSerializer.Meta.fields + ['students']