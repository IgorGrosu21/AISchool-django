from rest_framework.serializers import ModelSerializer, TimeField

from api.models import Lesson

from ...name import SubjectNameSerializer
from ..person import TeacherSerializer

class LessonSerializer(ModelSerializer):
  subject_name = SubjectNameSerializer()
  starting = TimeField(format='%H:%M')
  ending = TimeField(format='%H:%M')
  teacher = TeacherSerializer()
  
  class Meta:
    exclude = ['id']
    model = Lesson