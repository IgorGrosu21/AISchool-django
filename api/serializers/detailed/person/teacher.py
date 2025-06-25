from ...name import SubjectNameSerializer
from ...listed import PositionSerializer, TeacherSerializer
from .person import DetailedPersonSerializer

class DetailedTeacherSerializer(DetailedPersonSerializer, TeacherSerializer):
  subject_names = SubjectNameSerializer(many=True)
  work_places = PositionSerializer(many=True)
  
  class Meta(TeacherSerializer.Meta):
    fields = TeacherSerializer.Meta.fields + ['user', 'experience', 'subject_names', 'work_places']
    nested_fields = {
      'one': {
        **TeacherSerializer.Meta.nested_fields.get('one', {}),
      },
      'many': {
        **TeacherSerializer.Meta.nested_fields.get('many', {}),
        'subject_names': 'retrieve',
        'work_places': 'mutate'
      },
    }