from .progress import ProgressSerializer
from ...listed import ModuleSerializer, SubjectSerializer

class DetailedSubjectSerializer(ProgressSerializer, SubjectSerializer):
  modules = ModuleSerializer(many=True)
  
  class Meta(SubjectSerializer.Meta):
    fields = SubjectSerializer.Meta.fields + ProgressSerializer.Meta.fields + ['modules']