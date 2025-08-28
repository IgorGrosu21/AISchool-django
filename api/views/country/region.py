from rest_framework import generics
from drf_spectacular.utils import extend_schema

from api.models import Region
from api.serializers import RegionNameSerializer

@extend_schema(tags=['api / country'])
class RegionNamesView(generics.ListAPIView):
  authentication_classes = []
  permission_classes = []
  
  queryset = Region.objects.only('id', 'name')
  serializer_class = RegionNameSerializer
  
  def get_queryset(self):
    country = self.kwargs.get('country_slug')
    return self.queryset.filter(country__slug=country)