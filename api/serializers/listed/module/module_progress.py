from rest_framework.serializers import ModelSerializer

from api.models import ModuleProgress

from .module import ModuleSerializer
from .priceable import TheorySerializer, TaskSerializer

class ModuleProgressSerializer(ModelSerializer):
  module = ModuleSerializer(read_only=True)
  completed_theories = TheorySerializer(many=True, read_only=True)
  completed_tasks = TaskSerializer(many=True, read_only=True)
  
  class Meta:
    exclude = ['id', 'student']
    model = ModuleProgress