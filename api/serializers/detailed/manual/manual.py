from .progress import ProgressSerializer
from ...listed import ModuleSerializer, ManualSerializer

class DetailedManualSerializer(ProgressSerializer, ManualSerializer):
  modules = ModuleSerializer(many=True)
  
  class Meta(ManualSerializer.Meta):
    fields = ManualSerializer.Meta.fields + ['progress', 'modules']