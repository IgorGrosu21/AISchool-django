from rest_framework import generics
from drf_spectacular.utils import extend_schema

from api.models import City
from api.serializers import CityNameSerializer, DetailedCitySerializer

@extend_schema(tags=['api / country'])
class CityNamesView(generics.ListAPIView):
  authentication_classes = []
  permission_classes = []
  
  queryset = City.objects.only('id', 'name')
  serializer_class = CityNameSerializer
  
  def get_queryset(self):
    country_slug, region_slug = self.kwargs.get('country_slug'), self.kwargs.get('region_slug')
    return self.queryset.filter(region__country__slug=country_slug, region__slug=region_slug)

@extend_schema(tags=['api / country'])
class DetailedCityView(generics.RetrieveAPIView):
  queryset = City.objects.all()
  serializer_class = DetailedCitySerializer
  
  def get_object(self):
    return self.request.user.user.city