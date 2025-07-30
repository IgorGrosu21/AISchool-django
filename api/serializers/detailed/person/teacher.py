from ...name import SubjectNameSerializer
from ...listed import PositionSerializer, TeacherSerializer
from .person import DetailedPersonSerializer

class DetailedTeacherSerializer(DetailedPersonSerializer, TeacherSerializer):
  subjects = SubjectNameSerializer(many=True)
  work_places = PositionSerializer(many=True)
  
  class Meta(TeacherSerializer.Meta):
    fields = TeacherSerializer.Meta.fields + ['user', 'experience', 'subjects', 'work_places']
    nested_fields = {
      'one': {
        **TeacherSerializer.Meta.nested_fields.get('one', {}),
      },
      'many': {
        **TeacherSerializer.Meta.nested_fields.get('many', {}),
        'subjects': 'retrieve',
        'work_places': 'mutate'
      },
    }