from ..school import KlassSerializer
from ..person import TeacherSerializer
from ...name import LessonNameSerializer, LessonTimeNameSerializer

class LessonSerializer(LessonNameSerializer):
  lesson_time = LessonTimeNameSerializer()
  teacher = TeacherSerializer()
  klass = KlassSerializer()
  
  class Meta(LessonNameSerializer.Meta):
    fields = LessonNameSerializer.Meta.fields + ['lesson_time']
    nested_fields = {
      'one': {
        **LessonNameSerializer.Meta.nested_fields.get('one', {}),
        'lesson_time': 'retrieve'
      }
    }