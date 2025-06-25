from rest_framework import generics

from api.models import Module
from api.serializers import DetailedModuleSerializer
    
class DetailedModuleView(generics.RetrieveAPIView):
  queryset = Module.objects.all()
  serializer_class = DetailedModuleSerializer
  
  def get_object(self):
    subject_slug, slug = self.kwargs.get('subject_slug'), self.kwargs.get('slug')
    return self.queryset.filter(subject__slug=subject_slug).get(slug=slug)