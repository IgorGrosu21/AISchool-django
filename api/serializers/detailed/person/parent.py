from ...listed import ParentSerializer, StudentWithKlassSerializer
from .person import DetailedPersonSerializer, PersonHomeSerializer
from .student import StudentHomeSerializer

class DetailedParentSerializer(DetailedPersonSerializer, ParentSerializer):
  students = StudentWithKlassSerializer(many=True)

  class Meta(ParentSerializer.Meta):
    fields = ParentSerializer.Meta.fields + ['students']
    nested_fields = {
      'one': {
        **ParentSerializer.Meta.nested_fields.get('one', {}),
      },
      'many': {
        'students': 'retrieve'
      }
    }

class ParentHomeSerializer(PersonHomeSerializer):
  students = StudentHomeSerializer(many=True, read_only=True)