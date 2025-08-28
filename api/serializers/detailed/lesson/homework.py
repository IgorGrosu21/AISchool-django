from ...name import NoteNameSerializer
from ...listed import SpecificLessonSerializer, HomeworkSerializer, StudentSerializer

from ..._helpers import RelatedSerializer

class DetailedHomeworkSerializer(RelatedSerializer, HomeworkSerializer):
  specific_lesson = SpecificLessonSerializer()
  note = NoteNameSerializer(read_only=True, allow_null=True)
  student = StudentSerializer(read_only=True)
  
  class Meta(HomeworkSerializer.Meta):
    fields = HomeworkSerializer.Meta.fields + ['specific_lesson', 'note']
    nested_fields = {
      'one': {
        'specific_lesson': 'retrieve'  
      }
    }