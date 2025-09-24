from rest_framework.serializers import ModelSerializer

from api.models import Manual

from ...name import SubjectNameSerializer

class ManualSerializer(ModelSerializer):
  subject = SubjectNameSerializer(read_only=True)

  class Meta:
    fields = ['id', 'subject', 'grade', 'slug']
    model = Manual