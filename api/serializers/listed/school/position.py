from rest_framework.serializers import ModelSerializer, CharField

from api.models import Position

from ..person import TeacherSerializer
from ...name import SchoolNameSerializer, SubjectNameSerializer

class PositionSerializer(ModelSerializer):
  id = CharField(allow_blank=True, required=True)
  teacher = TeacherSerializer()
  subject_names = SubjectNameSerializer(many=True)
  school = SchoolNameSerializer()
  
  class Meta:
    fields = ['id', 'teacher', 'school', 'type', 'is_manager', 'subject_names']
    model = Position