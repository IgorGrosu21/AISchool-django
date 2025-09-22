from rest_framework.serializers import Serializer, UUIDField, TimeField, CharField, IntegerField

from ...name import LessonNameSerializer

class TomorrowTimetableSerializer(Serializer):
  id = UUIDField(read_only=True)
  starting = TimeField(read_only=True, format='%H:%M')
  ending = TimeField(read_only=True, format='%H:%M')
  weekday = CharField(read_only=True, max_length=2)
  order = IntegerField(read_only=True)
  school = UUIDField(read_only=True)
  lessons = LessonNameSerializer(many=True, read_only=True)