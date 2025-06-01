from rest_framework.serializers import ModelSerializer, UUIDField

from api.models import School

from ...media import MediaSerializer
from ..country import CityNameSerializer

class SchoolNameSerializer(ModelSerializer):
  id = UUIDField()
  city = CityNameSerializer(read_only=True)
  preview = MediaSerializer(read_only=True)
  
  class Meta:
    fields = ['id', 'name', 'city', 'preview']
    model = School