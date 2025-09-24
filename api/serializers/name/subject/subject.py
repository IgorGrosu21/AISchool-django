from api.models import Subject

from ..._helpers import RetrieveableSerializer

class SubjectNameSerializer(RetrieveableSerializer):
  class Meta:
    fields = ['id', 'image', 'verbose_name', 'slug']
    model = Subject
    extra_kwargs = {
      'verbose_name': {'read_only': True},
      'slug': {'read_only': True}
    }

class SubjectNameWithNotesSerializer(SubjectNameSerializer):
  class Meta(SubjectNameSerializer.Meta):
    fields = SubjectNameSerializer.Meta.fields + ['has_notes']