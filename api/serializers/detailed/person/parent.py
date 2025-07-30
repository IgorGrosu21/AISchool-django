from ...name import StudentNameSerializer
from ...listed import ParentSerializer
from .person import DetailedPersonSerializer

class DetailedParentSerializer(DetailedPersonSerializer, ParentSerializer):
  students = StudentNameSerializer(many=True)
  
  class Meta(ParentSerializer.Meta):
    fields = ParentSerializer.Meta.fields + ['user', 'students']
    nested_fields = {
      'one': {
        **ParentSerializer.Meta.nested_fields.get('one', {}),
      },
      'many': {
        'students': 'retrieve'
      }
    }