from rest_framework.serializers import ModelSerializer

from api.models import Region

class RegionNameSerializer(ModelSerializer):
  class Meta:
    fields = ['id', 'name', 'slug']
    model = Region