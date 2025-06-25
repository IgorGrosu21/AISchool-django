from rest_framework.serializers import CharField

from api.models import School

from ...name import LessonNameSerializer, LessonTimeNameSerializer

from ..._helpers import EditableSerializer

class LessonTimeSerializer(LessonTimeNameSerializer, EditableSerializer):
  lessons = LessonNameSerializer(many=True)
  
  class Meta(LessonTimeNameSerializer.Meta):
    fields = LessonTimeNameSerializer.Meta.fields + ['lessons', 'school']
    nested_fields = {
      'many': {
        'lessons': 'mutate'
      }
    }