from ...listed import RegionSerializer

from .country import DetailedCountrySerializer

class DetailedRegionSerializer(RegionSerializer):
  country = DetailedCountrySerializer()