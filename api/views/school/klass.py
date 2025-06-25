from rest_framework import generics

from api.models import Klass, School
from api.serializers import DetailedKlassSerializer, KlassWithDiarySerializer, SchoolWithKlassesSerializer

class SchoolKlassesView(generics.RetrieveUpdateAPIView):
  queryset = School.objects.all()
  serializer_class = SchoolWithKlassesSerializer

class DetailedKlassView(generics.RetrieveUpdateAPIView):
  queryset = Klass.objects.all()
  serializer_class = DetailedKlassSerializer
  
class KlassWithDiaryView(generics.RetrieveAPIView):
  queryset = Klass.objects.all()
  serializer_class = KlassWithDiarySerializer