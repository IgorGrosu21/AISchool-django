from rest_framework.serializers import SerializerMethodField

from api.models import School

from ...media import MediaSerializer
from ..country import CityNameSerializer
from ..lesson import LessonTimeNameSerializer
from .position import PositionNameSerializer
from ..._helpers import RetrieveableSerializer

class SchoolNameSerializer(RetrieveableSerializer):
  city = CityNameSerializer(read_only=True)
  preview = MediaSerializer(read_only=True)
  
  class Meta:
    fields = ['id', 'name', 'city', 'preview', 'slug']
    model = School

class SchoolNameWithTimeTableSerializer(SchoolNameSerializer):
  staff = PositionNameSerializer(many=True, read_only=True)
  timetable = LessonTimeNameSerializer(many=True, read_only=True)
  holidays = SerializerMethodField()
  
  def get_holidays(self, obj: School) -> list[dict[str, str]]:
    holidays_raw = obj.holidays if obj.holidays else []
    return [{'start': holiday.split('-')[0], 'end': holiday.split('-')[1]} for holiday in holidays_raw]
  
  class Meta(SchoolNameSerializer.Meta):
    fields = SchoolNameSerializer.Meta.fields + ['subjects', 'staff', 'timetable', 'holidays']