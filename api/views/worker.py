from rest_framework.views import APIView, Response
from drf_spectacular.utils import extend_schema
from api import models
import os

def create_folders():
  base_path = 'media/theories'
  for subject in models.Manual.objects.all():
    subject_dir = f'{base_path}/{subject.slug}'
    if not os.path.exists(subject_dir):
      os.makedirs(subject_dir)
    for module in subject.modules.all():
      module_dir = f'{subject_dir}/{module.slug}'
      if not os.path.exists(module_dir):
        os.makedirs(module_dir)
      for topic in module.topics.all():
        topic_dir = f'{module_dir}/{topic.slug}'
        if not os.path.exists(topic_dir):
          os.makedirs(topic_dir)

@extend_schema(exclude=True)
class WorkerView(APIView):
  authentication_classes = []
  permission_classes = []
  
  def get(self, request, *args, **kwargs):
    return Response()