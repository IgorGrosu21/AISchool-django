from ...name import NoteNameSerializer
from ...listed import SpecificLessonSerializer, HomeworkSerializer, StudentSerializer

from ..._helpers import RelatedSerializer

class DetailedSpecificLessonSerializer(RelatedSerializer, SpecificLessonSerializer):
  notes = NoteNameSerializer(many=True, required=False)
  homeworks = HomeworkSerializer(many=True, read_only=True)
  students = StudentSerializer(many=True, read_only=True)
  
  class Meta(SpecificLessonSerializer.Meta):
    fields = SpecificLessonSerializer.Meta.fields + ['notes', 'homeworks', 'students']
    nested_fields = {
      'one': {
        'lesson': 'retrieve'
      },
      'many': {
        'notes': 'mutate'
      }
    }