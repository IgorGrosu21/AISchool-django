from rest_framework.serializers import TimeField

from api.models import LessonTime

from ..._helpers import CreatableSerializer

class LessonTimeNameSerializer(CreatableSerializer):
  starting = TimeField(format='%H:%M')
  ending = TimeField(format='%H:%M')

  class Meta:
    fields = ['id', 'starting', 'ending', 'weekday', 'order']
    model = LessonTime