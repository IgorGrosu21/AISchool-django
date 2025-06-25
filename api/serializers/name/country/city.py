from rest_framework.serializers import ModelSerializer, UUIDField

from api.models import City

class CityNameSerializer(ModelSerializer):
  id = UUIDField()
  
  class Meta:
    fields = ['id', 'name']
    model = City