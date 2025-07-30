from ...name import SchoolNameSerializer, KlassNameSerializer

from ..._helpers import RelatedSerializer

class KlassSerializer(KlassNameSerializer, RelatedSerializer):
  school = SchoolNameSerializer()
  
  class Meta(KlassNameSerializer.Meta):
    fields = KlassNameSerializer.Meta.fields + ['school', 'networth']
    nested_fields = {
      'one': {
        'school': 'retrieve'
      }
    }