from ...name import SchoolNameSerializer, KlassNameSerializer

class KlassSerializer(KlassNameSerializer):
  school = SchoolNameSerializer()
  
  class Meta(KlassNameSerializer.Meta):
    fields = KlassNameSerializer.Meta.fields + ['school', 'networth']
    nested_fields = {
      'one': {
        'school': 'retrieve'
      }
    }