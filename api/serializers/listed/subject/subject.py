from rest_framework.serializers import ModelSerializer, UUIDField

from api.models import Subject

from ...name import SubjectNameSerializer

class SubjectSerializer(ModelSerializer):
  id = UUIDField()
  name = SubjectNameSerializer(read_only=True)
  
  class Meta:
    fields = ['id', 'name', 'grade']
    model = Subject