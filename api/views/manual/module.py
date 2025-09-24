from rest_framework import generics
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.models import Module
from api.serializers import DetailedModuleSerializer

@extend_schema(tags=['api / manual'])
class DetailedModuleView(generics.RetrieveAPIView):
  queryset = Module.objects.all()
  serializer_class = DetailedModuleSerializer

  def get_object(self):
    kwargs = {
      'manual__slug': self.kwargs.get('manual_slug'),
      'slug': self.kwargs.get('slug')
    }
    return get_object_or_404(self.queryset, **kwargs)