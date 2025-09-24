from .progress import ProgressSerializer
from ...listed import ModuleSerializer, ManualSerializer

class DetailedModuleSerializer(ProgressSerializer, ModuleSerializer):
  manual = ManualSerializer()

  class Meta(ModuleSerializer.Meta):
    fields = ModuleSerializer.Meta.fields + ['progress', 'manual']