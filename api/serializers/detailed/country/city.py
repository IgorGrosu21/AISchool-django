from ...listed import CitySerializer

class DetailedCitySerializer(CitySerializer):
  class Meta(CitySerializer.Meta):
    fields = '__all__'