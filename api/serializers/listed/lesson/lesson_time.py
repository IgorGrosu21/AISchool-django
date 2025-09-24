from ...name import LessonNameSerializer, LessonTimeNameSerializer

from ..._helpers import RelatedSerializer

class LessonTimeSerializer(LessonTimeNameSerializer, RelatedSerializer):
  lessons = LessonNameSerializer(many=True)

  class Meta(LessonTimeNameSerializer.Meta):
    fields = LessonTimeNameSerializer.Meta.fields + ['lessons', 'school']
    nested_fields = {
      'many': {
        'lessons': 'mutate'
      }
    }