from rest_framework.serializers import ModelSerializer

from api.models import Subject

class SubjectNameSerializer(ModelSerializer):
  class Meta:
    fields = ['id', 'image', 'verbose_name']
    model = Subject