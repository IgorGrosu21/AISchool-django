from ...name import RegionNameSerializer, CountryNameSerializer

class RegionSerializer(RegionNameSerializer):
  country = CountryNameSerializer()

  class Meta(RegionNameSerializer.Meta):
    fields = '__all__'