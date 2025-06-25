from .person import PersonSerializer
from ...name import TeacherNameSerializer

class TeacherSerializer(PersonSerializer, TeacherNameSerializer):
  class Meta(PersonSerializer.Meta, TeacherNameSerializer.Meta):
    pass