from rest_framework import generics
from drf_spectacular.utils import extend_schema

from api.permisions import IsTeacherOrReadonly, CanEditKlass
from api.models import Klass
from api.serializers import DetailedKlassSerializer

@extend_schema(tags=['api / school'])
class DetailedKlassView(generics.RetrieveUpdateAPIView):
  queryset = Klass.objects.all()
  serializer_class = DetailedKlassSerializer
  permission_classes = [IsTeacherOrReadonly, CanEditKlass]
  
  @extend_schema(exclude=True)
  def patch(self, request, *args, **kwargs):
    pass