from ...name import CountryNameSerializer

class DetailedCountrySerializer(CountryNameSerializer):
  class Meta(CountryNameSerializer.Meta):
    fields = '__all__'