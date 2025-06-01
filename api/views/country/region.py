from rest_framework import generics

from api.models import Region
from api.serializers import RegionNameSerializer

class RegionNamesView(generics.ListAPIView):
  authentication_classes = []
  permission_classes = []
  
  queryset = Region.objects.only('id', 'name')
  serializer_class = RegionNameSerializer
  
  def get_queryset(self):
    country = self.kwargs.get('country_pk')
    return self.queryset.filter(country=country)