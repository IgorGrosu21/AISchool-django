from ...name import CityNameSerializer
from .region import RegionSerializer

class CitySerializer(CityNameSerializer):
  region = RegionSerializer(read_only=True)
  
  class Meta(CityNameSerializer.Meta):
    fields = CityNameSerializer.Meta.fields + ['region']