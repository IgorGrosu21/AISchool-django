from ...name import RegionNameSerializer

from .country import CountrySerializer

class RegionSerializer(RegionNameSerializer):
  country = CountrySerializer()
  
  class Meta(RegionNameSerializer.Meta):
    fields = '__all__'