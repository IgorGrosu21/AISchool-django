from .progress import ProgressSerializer
from ...listed import ModuleSerializer, ManualSerializer

class DetailedModuleSerializer(ProgressSerializer, ModuleSerializer):
  subject = ManualSerializer()
  
  class Meta(ModuleSerializer.Meta):
    fields = ModuleSerializer.Meta.fields + ['progress', 'subject']