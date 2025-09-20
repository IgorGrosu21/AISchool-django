from rest_framework import serializers
from ...name import NoteNameSerializer
from ...listed import SpecificLessonSerializer, HomeworkSerializer, StudentSerializer

from ..._helpers import RelatedSerializer

class DetailedSpecificLessonSerializer(RelatedSerializer, SpecificLessonSerializer):
  notes = NoteNameSerializer(many=True, required=False)
  homeworks = HomeworkSerializer(many=True, read_only=True)
  students = StudentSerializer(many=True, read_only=True)
  is_student = serializers.SerializerMethodField()
  
  def get_is_student(self, obj):
    request = self.context.get('request')
    if request and hasattr(request, 'user') and hasattr(request.user, 'user'):
      return request.user.user.is_student
    return False
  
  class Meta(SpecificLessonSerializer.Meta):
    fields = SpecificLessonSerializer.Meta.fields + ['notes', 'homeworks', 'students', 'is_student']
    nested_fields = {
      'one': {
        'lesson': 'retrieve'
      },
      'many': {
        'notes': 'mutate'
      }
    }