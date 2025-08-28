from api.models import City

from ..._helpers import RetrieveableSerializer

class CityNameSerializer(RetrieveableSerializer):
  class Meta:
    fields = ['id', 'name']
    model = City
    extra_kwargs = {
      'name': {'read_only': True}
    }