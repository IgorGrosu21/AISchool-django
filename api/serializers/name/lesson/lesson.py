from api.models import Lesson

from ..subject import SubjectNameSerializer
from ..person import TeacherNameSerializer
from ..school import KlassNameSerializer

from ..._helpers import RelatedSerializer, CreatableSerializer

class LessonNameSerializer(RelatedSerializer, CreatableSerializer):
  subject = SubjectNameSerializer()
  teacher = TeacherNameSerializer()
  klass = KlassNameSerializer()
  
  class Meta:
    fields = ['id', 'subject', 'teacher', 'klass', 'lesson_time', 'manual_slug']
    model = Lesson
    nested_fields = {
      'one': {
        'subject': 'retrieve',
        'teacher': 'retrieve',
        'klass': 'retrieve'
      }
    }