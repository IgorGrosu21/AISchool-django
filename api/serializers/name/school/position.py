from rest_framework.serializers import ModelSerializer

from api.models import Position

from ..person import TeacherNameSerializer
from ..subject import SubjectNameSerializer

class PositionNameSerializer(ModelSerializer):
  teacher = TeacherNameSerializer()
  subject_names = SubjectNameSerializer(many=True)
  
  class Meta:
    fields = ['teacher', 'subject_names']
    model = Position