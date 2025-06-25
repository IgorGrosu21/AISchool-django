from ...listed import CitySerializer

from .region import DetailedRegionSerializer

class DetailedCitySerializer(CitySerializer):
  region = DetailedRegionSerializer(read_only=True)