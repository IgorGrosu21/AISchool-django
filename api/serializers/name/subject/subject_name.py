from rest_framework.serializers import ModelSerializer, UUIDField

from api.models import SubjectName

from .subject_type import SubjectTypeSerializer

class SubjectNameSerializer(ModelSerializer):
  id = UUIDField()
  type = SubjectTypeSerializer(read_only=True)
  
  class Meta:
    fields = ['id', 'type', 'verbose_name']
    model = SubjectName