from rest_framework import generics
from drf_spectacular.utils import extend_schema

from api.models import Country
from api.serializers import CountryNameSerializer

@extend_schema(tags=['api / country'])
class CountryNamesView(generics.ListAPIView):
  authentication_classes = []
  permission_classes = []

  queryset = Country.objects.all()
  serializer_class = CountryNameSerializer