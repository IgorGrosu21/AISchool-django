from rest_framework.serializers import CharField, TimeField

from api.models import LessonTime

from ..._helpers import EditableSerializer

class LessonTimeNameSerializer(EditableSerializer):
  id = CharField(allow_blank=True, required=False)
  starting = TimeField(format='%H:%M')
  ending = TimeField(format='%H:%M')
  
  class Meta:
    fields = ['id', 'starting', 'ending', 'weekday', 'order']
    model = LessonTime