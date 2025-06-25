from rest_framework.serializers import CharField, SerializerMethodField

from api.models import Lesson, LessonTime

from ..subject import SubjectNameSerializer
from ..person import TeacherNameSerializer
from ..school import KlassNameSerializer

from ..._helpers import EditableSerializer

class LessonNameSerializer(EditableSerializer):
  id = CharField(required=False, allow_blank=True)
  subject_name = SubjectNameSerializer()
  teacher = TeacherNameSerializer()
  klass = KlassNameSerializer()
  subject_slug = SerializerMethodField()
  
  def get_subject_slug(self, obj: Lesson):
    return f'{obj.subject_name.type.name}-{obj.subject_name.lang}-{obj.klass.grade}'
  
  class Meta:
    fields = ['id', 'subject_name', 'teacher', 'klass', 'lesson_time', 'subject_slug']
    model = Lesson
    nested_fields = {
      'one': {
        'subject_name': 'retrieve',
        'teacher': 'retrieve',
        'klass': 'retrieve'
      }
    }