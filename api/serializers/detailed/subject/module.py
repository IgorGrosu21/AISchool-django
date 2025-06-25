from .progress import ProgressSerializer
from ...listed import ModuleSerializer, SubjectSerializer

class DetailedModuleSerializer(ProgressSerializer, ModuleSerializer):
  subject = SubjectSerializer()
  
  class Meta(ModuleSerializer.Meta):
    fields = ModuleSerializer.Meta.fields + ProgressSerializer.Meta.fields + ['subject']