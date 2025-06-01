from rest_framework import generics

from api.models import Klass
from api.serializers import KlassSerializer, DetailedKlassSerializer

class KlassListView(generics.ListCreateAPIView):
  queryset = Klass.objects.all()
  serializer_class = KlassSerializer
  
  def get_queryset(self):
    school = self.kwargs.get('school_pk')
    return self.queryset.filter(school=school)

class DetailedKlassView(generics.RetrieveUpdateAPIView):
  queryset = Klass.objects.all()
  serializer_class = DetailedKlassSerializer