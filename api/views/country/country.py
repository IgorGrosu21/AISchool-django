from rest_framework import generics

from api.models import Country
from api.serializers import CountryNameSerializer

class CountryNamesView(generics.ListAPIView):
  authentication_classes = []
  permission_classes = []
  
  queryset = Country.objects.all()
  serializer_class = CountryNameSerializer