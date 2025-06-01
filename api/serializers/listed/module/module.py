from rest_framework.serializers import ModelSerializer

from api.models import Module

class ModuleSerializer(ModelSerializer):
  class Meta:
    fields = '__all__'
    model = Module