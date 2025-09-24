from rest_framework.serializers import ModelSerializer

from api.models import Position

from ..person import TeacherNameSerializer
from ..subject import SubjectNameSerializer

class PositionNameSerializer(ModelSerializer):
  teacher = TeacherNameSerializer()
  subjects = SubjectNameSerializer(many=True)

  class Meta:
    fields = ['teacher', 'subjects']
    model = Position