from api.models import Group

from ..subject import SubjectNameSerializer
from ..person import TeacherNameSerializer, StudentNameSerializer

from ..._helpers import RelatedSerializer, CreatableSerializer

class GroupNameSerializer(RelatedSerializer, CreatableSerializer):
  subject = SubjectNameSerializer()
  teacher = TeacherNameSerializer(required=False, allow_null=True)
  students = StudentNameSerializer(many=True)
  
  class Meta:
    fields = ['id', 'order', 'klass', 'subject', 'teacher', 'students']
    model = Group
    nested_fields = {
      'one': {
        'subject': 'retrieve',
        'teacher': 'retrieve'
      },
      'many': {
        'students': 'retrieve'
      }
    }