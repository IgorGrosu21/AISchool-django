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
    region = self.kwargs.get('region_pk')
    return self.queryset.filter(region=region)

@extend_schema(tags=['api / country'])
class DetailedCityView(generics.RetrieveAPIView):
  queryset = City.objects.all()
  serializer_class = DetailedCitySerializer
  
  def get_object(self):
    return self.request.user.user.city