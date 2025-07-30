from ...listed import SpecificLessonSerializer, NoteSerializer, HomeworkSerializer, StudentSerializer

from ..._helpers import RelatedSerializer

class DetailedSpecificLessonSerializer(RelatedSerializer, SpecificLessonSerializer):
  notes = NoteSerializer(many=True)
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