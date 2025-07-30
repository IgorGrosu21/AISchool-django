from rest_framework.serializers import ModelSerializer

from api.models import City

class CityNameSerializer(ModelSerializer):
  class Meta:
    fields = ['id', 'name']
    model = City