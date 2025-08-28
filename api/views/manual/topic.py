from rest_framework import generics
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.models import Topic
from api.serializers import DetailedTopicSerializer
    
@extend_schema(tags=['api / manual'])
class DetailedTopicView(generics.RetrieveAPIView):
  queryset = Topic.objects.all()
  serializer_class = DetailedTopicSerializer
  
  def get_object(self):
    kwargs = {
      'module__manual__slug': self.kwargs.get('manual_slug'),
      'module__slug': self.kwargs.get('module_slug'),
      'slug': self.kwargs.get('slug')
    }
    return get_object_or_404(self.queryset, **kwargs)