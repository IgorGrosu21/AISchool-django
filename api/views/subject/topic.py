from rest_framework import generics

from api.models import Topic
from api.serializers import DetailedTopicSerializer
    
class DetailedTopicView(generics.RetrieveAPIView):
  queryset = Topic.objects.all()
  serializer_class = DetailedTopicSerializer
  
  def get_object(self):
    subject_slug, module_slug, slug = self.kwargs.get('subject_slug'), self.kwargs.get('module_slug'), self.kwargs.get('slug')
    return self.queryset.filter(module__subject__slug=subject_slug, module__slug=module_slug).get(slug=slug)