from ...name import CountryNameSerializer

class CountrySerializer(CountryNameSerializer):
  class Meta(CountryNameSerializer.Meta):
    fields = '__all__'