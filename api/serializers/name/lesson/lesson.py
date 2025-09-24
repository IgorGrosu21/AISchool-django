from api.models import Lesson

from ..subject import SubjectNameWithNotesSerializer
from ..person import TeacherNameSerializer

from ..._helpers import RelatedSerializer, CreatableSerializer

class LessonNameSerializer(RelatedSerializer, CreatableSerializer):
  subject = SubjectNameWithNotesSerializer()
  teacher = TeacherNameSerializer()

  class Meta:
    fields = ['id', 'subject', 'teacher', 'klass', 'lesson_time', 'klass_slug', 'manual_slug']
    model = Lesson
    nested_fields = {
      'one': {
        'subject': 'retrieve',
        'teacher': 'retrieve'
      }
    }