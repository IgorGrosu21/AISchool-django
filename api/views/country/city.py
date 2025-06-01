from rest_framework import generics

from api.models import City
from api.serializers import CityNameSerializer, DetailedCitySerializer

class CityNamesView(generics.ListAPIView):
  authentication_classes = []
  permission_classes = []
  
  queryset = City.objects.only('id', 'name')
  serializer_class = CityNameSerializer
  
  def get_queryset(self):
    region = self.kwargs.get('region_pk')
    return self.queryset.filter(region=region)

class CityView(generics.RetrieveAPIView):
  queryset = City.objects.all()
  serializer_class = DetailedCitySerializer
  
  def get_object(self):
    return self.request.user.user.city