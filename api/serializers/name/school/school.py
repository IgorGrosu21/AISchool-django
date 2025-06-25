from rest_framework.serializers import ModelSerializer, UUIDField

from api.models import School

from ...media import MediaSerializer
from ..country import CityNameSerializer
from ..lesson import LessonTimeNameSerializer
from .position import PositionNameSerializer

class SchoolNameSerializer(ModelSerializer):
  id = UUIDField()
  city = CityNameSerializer(read_only=True)
  preview = MediaSerializer(read_only=True)
  
  class Meta:
    fields = ['id', 'name', 'city', 'preview']
    model = School

class SchoolNameWithTimeTableSerializer(SchoolNameSerializer):
  staff = PositionNameSerializer(many=True, read_only=True)
  timetable = LessonTimeNameSerializer(many=True, read_only=True)
  
  class Meta(SchoolNameSerializer.Meta):
    fields = SchoolNameSerializer.Meta.fields + ['staff', 'timetable']