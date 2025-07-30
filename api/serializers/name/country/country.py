from rest_framework.serializers import ModelSerializer

from api.models import Country

class CountryNameSerializer(ModelSerializer):
  class Meta:
    fields = ['id', 'name', 'flag']
    model = Country