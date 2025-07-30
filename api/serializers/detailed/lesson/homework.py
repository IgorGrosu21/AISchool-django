from ...listed import NoteSerializer, SpecificLessonSerializer, HomeworkSerializer, StudentSerializer

from ..._helpers import RelatedSerializer

class DetailedHomeworkSerializer(RelatedSerializer, HomeworkSerializer):
  specific_lesson = SpecificLessonSerializer()
  note = NoteSerializer(read_only=True, allow_null=True)
  student = StudentSerializer(read_only=True)
  
  class Meta(HomeworkSerializer.Meta):
    fields = HomeworkSerializer.Meta.fields + ['specific_lesson', 'note']
    nested_fields = {
      'one': {
        'specific_lesson': 'retrieve'  
      }
    }