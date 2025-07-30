from .lesson import LessonSerializer
from ...name import SpecificLessonNameSerializer
from ...media import DetailedMediaSerializer

class SpecificLessonSerializer(SpecificLessonNameSerializer):
  lesson = LessonSerializer()
  files = DetailedMediaSerializer(many=True, read_only=True)
  
  class Meta(SpecificLessonNameSerializer.Meta):
    fields = SpecificLessonNameSerializer.Meta.fields + ['files', 'links']